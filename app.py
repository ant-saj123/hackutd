import csv
import streamlit as st

# Read data from the CSV file
def read_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

# Evaluate homebuyers and provide suggestions
def evaluate_homebuyers(data):
    results = []
    # Skip the first row (column names) when processing the data
    for idx, buyer in enumerate(data, start = 1):
        if idx == 1:
            continue
        credit_rating = int(buyer['CreditScore'])
        ltv = ((float(buyer['AppraisedValue']) - float(buyer['DownPayment'])) / float(buyer['AppraisedValue'])) * 100
        dti = (float(buyer['CarPayment']) + float(buyer['CreditCardPayment']) +
               float(buyer['StudentLoanPayments']) + float(buyer['MonthlyMortgagePayment'])) / float(buyer['GrossMonthlyIncome']) * 100
        fedti = float(buyer['MonthlyMortgagePayment']) / float(buyer['GrossMonthlyIncome']) * 100
        
        if credit_rating >= 640 and ltv < 80 and dti <= 43 and fedti <= 28:
            results.append('Y')  # Approved
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
            results.append('N ' + ', '.join(suggestions))  # Not Approved with suggestions
    return results
def main():
    st.title('Homebuyer Evaluation Results')

    # Specify the file path
    file_path = r'C:\Users\Antony Sajesh\OneDrive\Desktop\hackutd\HackUTD-2023-HomeBuyerInfo.csv'
    data = read_data(file_path)
    results = evaluate_homebuyers(data)

    # Display results in a table
    st.table(results)

if __name__ == "__main__":
    main()