import pandas as pd
from sklearn.model_selection import train_test_split

def preprocess_data(file_path):
    """Load and preprocess the data."""
    df = pd.read_csv(file_path)
    df.drop(['customerID'], axis=1, inplace=True)
    df.fillna(df.mean(), inplace=True)
    return df

def split_data(df):
    """Split the data into training and testing sets."""
    X = df.drop('Churn', axis=1)
    y = df['Churn']
    return train_test_split(X, y, test_size=0.2, random_state=42)
