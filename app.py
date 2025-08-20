import streamlit as st
import pandas as pd

st.set_page_config(page_title="Optimal HRA Split", page_icon="💸")
st.title("Optimal HRA Split Calculator")
st.caption("Rule: Exemption = min(HRA, 50% of Balance Figure), where Balance = Salary − HRA")

# Input: only total salary
S = st.number_input("Enter your total salary (₹)", min_value=0, step=1000, value=0)

if S > 0:
    # Optimal HRA
    H_opt = S / 3
    exemption_opt = S / 3

    st.subheader("📌 Optimal Split")
    st.metric("Optimal HRA", f"₹{H_opt:,.0f}")
    st.metric("Maximum Exemption", f"₹{exemption_opt:,.0f}")

    # Scenario table around optimal HRA
    st.subheader("🔎 Scenarios Around Optimal HRA")
    hra_values, balance_values, half_balance_values, exemptions = [], [], [], []

    for pct in range(-20, 25, 5):  # -20%, -15%, ..., +20%
        H = H_opt * (1 + pct/100)
        balance = S - H
        half_balance = balance / 2
        exemption = min(H, half_balance)

        hra_values.append(round(H))
        balance_values.append(round(balance))
        half_balance_values.append(round(half_balance))
        exemptions.append(round(exemption))

    df = pd.DataFrame({
        "HRA (₹)": hra_values,
        "Balance Figure (₹)": balance_values,
        "50% of Balance (₹)": half_balance_values,
        "Exemption (₹)": exemptions
    })

    # Highlight the row with maximum exemption
    def highlight_max(s):
        is_max = s == df["Exemption (₹)"].max()
        return ['background-color: #d4edda; font-weight: bold' if v else '' for v in is_max]

    styled_df = df.style.apply(highlight_max, subset=["Exemption (₹)"])

    st.dataframe(styled_df, use_container_width=True)

    # Optional: chart for visualization
    st.subheader("📈 Exemption vs HRA")
    st.line_chart(df.set_index("HRA (₹)")["Exemption (₹)"])
