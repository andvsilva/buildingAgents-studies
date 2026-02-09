import mlflow
import mlflow.sklearn

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error

from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor


def main():
    # -----------------------------
    # Load data
    # -----------------------------
    X, y = load_diabetes(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # -----------------------------
    # MLflow experiment
    # -----------------------------
    mlflow.set_experiment("multi-model-multi-params")

    # -----------------------------
    # Models & parameter grids
    # -----------------------------
    models = {
        "LinearRegression": {
            "class": LinearRegression,
            "params": [{}]
        },
        "Ridge": {
            "class": Ridge,
            "params": [
                {"alpha": 0.01},
                {"alpha": 0.1},
                {"alpha": 1.0},
                {"alpha": 10.0},
            ]
        },
        "Lasso": {
            "class": Lasso,
            "params": [
                {"alpha": 0.01},
                {"alpha": 0.1},
                {"alpha": 1.0},
            ]
        },
        "RandomForest": {
            "class": RandomForestRegressor,
            "params": [
                {"n_estimators": 50, "max_depth": 5, "random_state": 42},
                {"n_estimators": 100, "max_depth": 5, "random_state": 42},
                {"n_estimators": 100, "max_depth": 10, "random_state": 42},
            ]
        }
    }

    # -----------------------------
    # Run experiments
    # -----------------------------
    with mlflow.start_run(run_name="all_models"):
        for model_name, cfg in models.items():
            ModelClass = cfg["class"]

            for params in cfg["params"]:
                with mlflow.start_run(
                    nested=True,
                    run_name=model_name
                ):
                    model = ModelClass(**params)
                    model.fit(X_train, y_train)

                    preds = model.predict(X_test)
                    rmse = root_mean_squared_error(y_test, preds)

                    mlflow.log_param("model_name", model_name)
                    mlflow.log_params(params)
                    mlflow.log_metric("rmse", rmse)

                    mlflow.sklearn.log_model(
                        model,
                        artifact_path="model"
                    )

                    print(
                        f"{model_name} | {params} | RMSE={rmse:.2f}"
                    )


if __name__ == "__main__":
    main()
