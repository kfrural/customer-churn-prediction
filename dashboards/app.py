import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('../data/processed_churn_data.csv')

# Data verification
if df.empty:
    raise ValueError("The DataFrame is empty. Check the file path and content.")

# Create the Dash app
app = dash.Dash(__name__)

# Layout of the application
app.layout = html.Div(style={'backgroundColor': '#f5f5f5', 'padding': '20px'}, children=[
    html.H1("Customer Churn Prediction", style={'textAlign': 'center', 'color': '#333'}),
    
    dcc.Graph(
        id='churn-by-tenure',
        figure=px.histogram(df, x='tenure', color='Churn', 
                             title='Churn by Tenure',
                             color_discrete_sequence=['#FF5733', '#3498DB'],  # Custom colors
                             template='plotly_white')  # White background template
    ),
    
    dcc.Graph(
        id='monthly-charges-vs-tenure',
        figure=px.scatter(df, x='MonthlyCharges', y='tenure', color='Churn',
                          title='Monthly Charges vs Tenure',
                          color_discrete_sequence=['#FF5733', '#3498DB'],  # Custom colors
                          template='plotly_white')  # White background template
    )
    
])

if __name__ == '__main__':
    app.run_server(debug=True)
