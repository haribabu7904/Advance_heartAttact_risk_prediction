import os
import joblib
from .model_stacking import build_stacked_model

def train_and_save(X_train, y_train, scaler, models_dir: str = 'models'):
    os.makedirs(models_dir, exist_ok=True)

    model = build_stacked_model()
    print('Training stacked model...')
    model.fit(X_train, y_train)

    # Save model and scaler
    joblib.dump(model, os.path.join(models_dir, 'meta_model.pkl'))
    joblib.dump(scaler, os.path.join(models_dir, 'scaler.pkl'))
    print(f'Model and scaler saved to: {models_dir}')
    
    return model
  
    return model
