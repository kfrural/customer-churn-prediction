import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('../data/telecom_churn_data.csv')

# Create a Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Customer Churn Prediction"),
    
    dcc.Graph(
        figure=px.histogram(df, x='tenure', color='Churn', title='Churn by Tenure')
    ),
    
    dcc.Graph(
        figure=px.scatter(df, x='MonthlyCharges', y='tenure', color='Churn', title='Monthly Charges vs Tenure')
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
