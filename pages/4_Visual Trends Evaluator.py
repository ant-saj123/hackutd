import streamlit as st
import pandas as pd
import plotly.express as px

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
            results.append([idx, 'Approved'])  # Approved
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
            results.append([idx, 'Declined', ', '.join(suggestions)])  # Not Approved with suggestions
    return results

# Define the pages
def homebuyer_evaluation_page():

    # Allow the user to upload a CSV file
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file is not None:
        # Read data from the uploaded file using Pandas
        data = pd.read_csv(uploaded_file)
        results = evaluate_homebuyers(data)

        # Display results in a customized table with adjusted headers using Pandas DataFrame
        st.markdown("### Mortgage Approval Results")
        df = pd.DataFrame(results, columns=["ID", "Status", "Message"])
        #st.write(df)

        if results:
            counts = {'Approved': 0, 'Declined': 0}
            solution_counts = {}

            # Create a mapping of full solutions to abbreviated solutions
            solution_abbreviations = {
                'Improve credit rating': 'Improve CR',
                'Increase down payment or look for a less expensive home': 'Inc. DP or Cheaper Home',
                'Pay off debt or transfer to lower interest loans/credit cards': 'Less debt or trans. to lower IL/CC',
                'Reduce housing expenses': 'Reduce HE'
            }

            for result in results:
                status = result[1]
                if status == 'Approved':
                    counts['Approved'] += 1
                elif status == 'Declined':
                    counts['Declined'] += 1
                    # Split the suggestions by ', ' and parse them
                    suggestions = result[2].split(', ')
                    for suggestion in suggestions:
                        # Use abbreviated solution if available, or the full suggestion
                        abbreviated_solution = solution_abbreviations.get(suggestion, suggestion)
                        # Count the solutions
                        solution_counts[abbreviated_solution] = solution_counts.get(abbreviated_solution, 0) + 1
                        #solution_counts[suggestion] = solution_counts.get(suggestion, 0) + 1

            # Plotting the results
            fig1 = px.bar(x=list(counts.keys()), y=list(counts.values()), labels={'x': 'Result', 'y': 'Count'})
            fig1.update_traces(texttemplate='%{y}', textposition='outside')
            fig1.update_layout(title='Number of Approvals and Rejections', xaxis_title='Result', yaxis_title='Count')

            fig2 = px.bar(x=list(solution_counts.keys()), y=list(solution_counts.values()),
                          labels={'x': 'Solution', 'y': 'Count'})
            fig2.update_traces(texttemplate='%{y}', textposition='outside')
            fig2.update_layout(title='Solutions for Rejections', xaxis_title='Solution', yaxis_title='Count')

            # Display the graphs
            st.plotly_chart(fig1)
            st.plotly_chart(fig2)
            st.info('**Atlas**\n\n'
            '- **Improve CR:** Improve credit rating\n'
            '- **Inc. DP or Cheaper Home:** Increase down payment or look for a less expensive home\n'
            '- **Less debt or trans. to lower IL/CC:** Pay off debt or transfer to lower interest loans/credit cards\n'
            '- **Reduce HE:** Reduce housing expenses')


def main():
    logoUrl = 'https://www.fanniemae.com/sites/g/files/koqyhd191/files/2020-10/fannie-mae-logo-dark-blue.png'
    st.image(logoUrl, width=300)
    st.header("Visual Trends Evaluator")
    homebuyer_evaluation_page()

if __name__ == "__main__":
    main()
