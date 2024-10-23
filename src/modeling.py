from sklearn.ensemble import RandomForestClassifier

def train_random_forest(X_train, y_train):
    """Train a RandomForest model."""
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model
