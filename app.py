import streamlit as st

st.title("HRA Tax Exemption Calculator")

# Input fields
income = st.number_input("Enter your total income (₹)", min_value=0, step=1000)
hra = st.number_input("Enter your HRA (₹)", min_value=0, step=1000)

if income > 0:
    # Tax exemption calculation
    exemption = min(hra, income / 2)

    st.subheader("💰 Tax Calculation")
    st.write(f"Total Income: ₹{income:,.0f}")
    st.write(f"HRA Claimed: ₹{hra:,.0f}")
    st.write(f"Exempted from Tax: ₹{exemption:,.0f}")

    # Optimal HRA suggestion
    optimal_hra = income / 2
    st.subheader("📌 Suggested Optimal HRA")
    st.write(f"Best possible HRA to maximize exemption = ₹{optimal_hra:,.0f}")
