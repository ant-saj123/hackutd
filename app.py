import csv
import streamlit as st
import plotly.express as px

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
            results.append('Yes')  # Approved
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
            results.append('No ' + ', '.join(suggestions))  # Not Approved with suggestions
    return results

def main():
    st.title('Homebuyer Evaluation Results')

    # Specify the file path
    file_path = r'C:\Users\Antony Sajesh\OneDrive\Desktop\hackutd\HackUTD-2023-HomeBuyerInfo.csv'
    data = read_data(file_path)
    results = evaluate_homebuyers(data)

    # Sidebar for navigation
    st.sidebar.title('Navigation')
    selected_page = st.sidebar.radio('Go to', ['Home', 'Graphs'])

    if selected_page == 'Home':
        # Display table for 'Home' page
        filtered_results = results  # Exclude the first row (column names)
        st.table(filtered_results)
    elif selected_page == 'Graphs':
        st.sidebar.write('## Graphs')
        
        # Count 'Y' and 'N' results
    counts = {'Yes': 0, 'No': 0}
    solutions_counts = {}

    # Create a mapping of full solutions to abbreviated solutions
    solution_abbreviations = {
        'Improve credit rating': 'Improve CR',
        'Increase down payment or look for a less expensive home': 'Inc. DP or Cheaper Home',
        'Pay off debt or transfer to lower interest loans/credit cards': 'Less debt or trans. to lower IL/CC',
        'Reduce housing expenses': 'Reduce HE' 
    }

    for result in results:
        status, *solutions = result.split(' ', 1)
        if status == 'Yes':
            counts['Yes'] += 1
        elif status == 'No':
            counts['No'] += 1
            for solution in solutions[0].split(', '):
                abbreviated_solution = solution_abbreviations.get(solution, solution)
                solutions_counts[abbreviated_solution] = solutions_counts.get(abbreviated_solution, 0) + 1

    # Plotting the results
    fig1 = px.bar(x=list(counts.keys()), y=list(counts.values()), labels={'x': 'Result', 'y': 'Count'}, text=list(counts.values()))
    fig1.update_traces(texttemplate='%{text}', textposition='outside')
    fig1.update_layout(title='Number of Approvals and Rejections', xaxis_title='Result', yaxis_title='Count')

    fig2 = px.bar(x=list(solutions_counts.keys()), y=list(solutions_counts.values()),
                  labels={'x': 'Solution', 'y': 'Count'}, text=list(solutions_counts.values()))
    fig2.update_traces(texttemplate='%{text}', textposition='outside')
    
    # Set x-axis tickangle to 0 for horizontal labels
    fig2.update_layout(title='Solutions for Rejections', xaxis_title='Solution', yaxis_title='Count', xaxis_tickangle=0)

    
    
    # Display the graphs
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)
    st.info('**Atlas**\n\n'
            '- **Improve CR:** Improve credit rating\n'
            '- **Inc. DP or Cheaper Home:** Increase down payment or look for a less expensive home\n'
            '- **Less debt or trans. to lower IL/CC:** Pay off debt or transfer to lower interest loans/credit cards\n'
            '- **Reduce HE:** Reduce housing expenses')

if __name__ == "__main__":
    main()