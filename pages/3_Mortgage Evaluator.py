import csv
import streamlit as st
import pandas as pd

# Evaluate homebuyers and provide suggestions
def evaluate_homebuyers(data):
    results = []
    # Skip the first row (column names) when processing the data
    for idx, buyer in enumerate(data.itertuples(), start=1):
        credit_rating = int(buyer.CreditScore)
        ltv = ((float(buyer.AppraisedValue) - float(buyer.DownPayment)) / float(buyer.AppraisedValue)) * 100
        dti = (float(buyer.CarPayment) + float(buyer.CreditCardPayment) +
               float(buyer.StudentLoanPayments) + float(buyer.MonthlyMortgagePayment)) / float(buyer.GrossMonthlyIncome) * 100
        fedti = float(buyer.MonthlyMortgagePayment) / float(buyer.GrossMonthlyIncome) * 100

        if credit_rating >= 640 and ltv < 80 and dti <= 43 and fedti <= 28:
            results.append([idx, 'Approved', 'Congratulations! You have been Approved!'])  # Approved
        else:
            suggestions = []
            if credit_rating < 640:
                suggestions.append('Improve credit rating')
            if ltv >= 80:
                suggestions.append('Increase down payment or look for a less expensive home')
            if dti > 43:
                suggestions.append('Pay off debt or transfer to lower interest loans/credit cards')
            if fedti > 28:
                suggestions.append('Reduce housing expenses')
            results.append([idx, 'Declined', 'Unfortunately, you have not been approved. We recommend you ' + ', '.join(suggestions)])  # Not Approved with suggestions
    return results

def main():
    logoUrl = 'https://www.fanniemae.com/sites/g/files/koqyhd191/files/2020-10/fannie-mae-logo-dark-blue.png'
    st.image(logoUrl, width=300)
    st.header('Homebuyer Evaluation')
    
    # Allow the user to upload a CSV file
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file is not None:
        # Read data from the uploaded file using Pandas
        data = pd.read_csv(uploaded_file)
        results = evaluate_homebuyers(data)

        # Display results in a customized table with adjusted headers using Pandas DataFrame
        st.markdown("### Mortgage Approval Results")
        df = pd.DataFrame(results, columns=["ID", "Status", "Message"])
        st.write(df)

if __name__ == "__main__":
    main()