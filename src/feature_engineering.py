import pandas as pd

def create_features(df):
    """Add interaction features."""
    df['monthly_tenure_interaction'] = df['MonthlyCharges'] * df['tenure']
    return df

