from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, classification_report
)

def evaluate(model, X_test, y_test):
    """Evaluate a trained model and print performance metrics."""
    
    # Predictions
    y_pred = model.predict(X_test)
    y_proba = None
    try:
        y_proba = model.predict_proba(X_test)[:, 1]
    except Exception:
        pass

    # Core metrics
    results = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred, zero_division=0),
        'recall': recall_score(y_test, y_pred, zero_division=0),
        'f1': f1_score(y_test, y_pred, zero_division=0),
    }

    # Optional ROC-AUC
    if y_proba is not None:
        try:
            results['roc_auc'] = roc_auc_score(y_test, y_proba)
        except Exception:
            results['roc_auc'] = None

    # Display
    print('--- Evaluation ---')
    for k, v in results.items():
        print(f'{k}: {v:.4f}' if v is not None else f'{k}: None')

    print('\nConfusion Matrix:')
    print(confusion_matrix(y_test, y_pred))
    print('\nClassification Report:')
    print(classification_report(y_test, y_pred, zero_division=0))

    return results
