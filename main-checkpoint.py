from src.data_preprocessing import load_data, preprocess_features
from src.model_training import train_and_save
from src.model_evaluation import evaluate
from src.utils import load_models


def main():   # ✅ Function defined correctly
    data_path = 'data/heart.csv'  # put your dataset here
    print('Loading data...')
    df = load_data(data_path)

    print('Preprocessing...')
    X_train, X_test, y_train, y_test, scaler = preprocess_features(df, target_col='target')

    print('Training...')
    model = train_and_save(X_train, y_train, scaler)

    print('Evaluating...')
    evaluate(model, X_test, y_test)

    print('Done.')  # ✅ All lines inside function properly indented


if __name__ == '__main__':  # ✅ Correct main guard
    main()
    