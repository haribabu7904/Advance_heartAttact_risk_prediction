# src/model_stacking.py

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, StackingClassifier
from sklearn.linear_model import LogisticRegression

def build_stacked_model():
    """Build and return a stacked ensemble model."""
    base_models = [
        ('rf', RandomForestClassifier(n_estimators=100, random_state=42)),
        ('gb', GradientBoostingClassifier(n_estimators=100, random_state=42))
    ]

    meta_model = LogisticRegression(max_iter=1000)

    stacked_model = StackingClassifier(
        estimators=base_models,
        final_estimator=meta_model,
        cv=5
    )

    return stacked_model
