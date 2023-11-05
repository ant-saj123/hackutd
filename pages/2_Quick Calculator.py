import streamlit as st

# Function to calculate LTV (Loan-to-Value) ratio
def calculate_ltv(appraised_value, down_payment):
    if appraised_value > 0:
        loan_amount = appraised_value - down_payment
        ltv = (float(loan_amount) / float(appraised_value)) * 100
        return ltv
    else:
        return 100  # Handle the case when appraised_value is zero

# Function to calculate DTI (Debt-to-Income) ratio
def calculate_dti(gross_income, car_payment, credit_card_payment, monthly_mortgage_payment):
    if gross_income > 0:
        monthly_debt = car_payment + credit_card_payment + monthly_mortgage_payment
        dti = (float(monthly_debt) / float(gross_income)) * 100.00
        return dti
    else:
        return 100  # Handle the case when gross_income is zero

# Function to calculate FEDTI (Front-end Debt-to-Income) ratio
def calculate_fedti(monthly_mortgage_payment, gross_income):
    if gross_income > 0:
        fedti = (float(monthly_mortgage_payment) / float(gross_income)) * 100.00
        return fedti
    else:
        return 100  # Handle the case when gross_income is zero

# Streamlit app
def main():
    logoUrl = 'https://www.fanniemae.com/sites/g/files/koqyhd191/files/2020-10/fannie-mae-logo-dark-blue.png'
    st.image(logoUrl, width=300)
    st.title("Mortgage Approval Calculator")

    st.text('Fill out all applicable information')

    # User inputs
    gross_income = st.number_input("Gross Monthly Income ($)", placeholder='$0', min_value=0.0, step=1.0)
    credit_card_payment = st.number_input("Monthly Credit Card Payment ($)", min_value=0.0, step=1.0)
    car_payment = st.number_input("Monthly Car Payment ($)", min_value=0.0, step=1.0)
    student_loan_payments = st.number_input("Monthly Student Loan Payments ($)", min_value=0.0, step=1.0)
    appraised_value = st.number_input("Appraised Value ($)", min_value=0.0, step=1.0)
    down_payment = st.number_input("Down Payment ($)", min_value=0.0, step=1.0)
    loan_amount = appraised_value - down_payment
    monthly_mortgage_payment = st.number_input("Monthly Mortgage Payment ($)", min_value=0.0, step=1.0)
    credit_score = st.slider('What is your credit score?', min_value=300, max_value=850, step=1)

    # Calculate LTV, DTI, and FEDTI
    ltv = calculate_ltv(appraised_value, down_payment)
    dti = calculate_dti(gross_income, car_payment, credit_card_payment, monthly_mortgage_payment)
    fedti = calculate_fedti(monthly_mortgage_payment, gross_income)

    # Mortgage approval conditions
    approved = (
        credit_score >= 640 and ltv < 80 and dti <= 43 and fedti <= 28
    )

    # Display results
    st.subheader("Mortgage Approval Results:")
    st.write(f"Loan-to-Value (LTV): {ltv:.2f}%")
    st.write(f"Debt-to-Income (DTI): {dti:.2f}%")
    st.write(f"Front-end Debt-to-Income (FEDTI): {fedti:.2f}%")

    if approved:
        st.success("Congratulations! You are approved for a mortgage.✔️")
    else:
        st.warning("Unfortunately, you do not meet the mortgage approval criteria")

if __name__ == "__main__":
    main()
