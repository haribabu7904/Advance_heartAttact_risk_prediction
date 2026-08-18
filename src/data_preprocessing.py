import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_data(path: str) -> pd.DataFrame:
    """Load CSV into DataFrame."""
    df = pd.read_csv(path)
    return df


def preprocess_features(df: pd.DataFrame, target_col: str = 'target'):
    """
    Basic preprocessing. Assumes dataset columns are numeric or already encoded.
    Returns scaled train/test splits and scaler object.
    """
    # Drop rows with missing target
    df = df.copy()
    df = df.dropna(subset=[target_col])

    # Optionally fill or drop other missing values
    df = df.fillna(df.median())

    X = df.drop(columns=[target_col])
    y = df[target_col].astype(int)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Standardize features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train.values, y_test.values, scaler
