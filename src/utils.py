import joblib
import os

def load_models(models_dir: str = 'models'):
    """Load the trained stacked model and scaler."""
    
    model_path = os.path.join(models_dir, 'meta_model.pkl')
    scaler_path = os.path.join(models_dir, 'scaler.pkl')

    # Check if both model and scaler exist
    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        raise FileNotFoundError(
            'Model or scaler not found. Please train the model first (run main.py).'
        )

    # Load model and scaler
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

    return model, scaler
