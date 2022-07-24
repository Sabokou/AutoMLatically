from typing import Dict
# explicitly require this experimental feature
from sklearn.experimental import enable_halving_search_cv # noqa
from sklearn.model_selection import HalvingRandomSearchCV, GridSearchCV


class ModelOptimizer:
    """
    This class is used to finetune models and optimize their hyperparameters.
    """

    def __init__(self):
        self.param_grids = {
            "linear_regression":({
                "linearregression__normalize":[True, False],
                "linearregression__positive": [True, False]
            }, "n_samples"),
            "sgd_regressor":({
                "sgdregressor__penalty": ["l2", "elasticnet"],
                "sgdregressor__alpha":[1e-3, 1e-4, 1e-5]
            }, "n_samples"),
            "mlp_regressor":({
                "mlpregressor__hidden_layer_sizes": [(100,1), (100,100,1), (64,128,32,1)],
                "mlpregressor__alpha": [1e-3, 1e-4, 1e-5]
            }, "n_samples"),
            "random_forest_regressor":({
                # "randomforestregressor__n_estimators": [10,50, 100, 250, 500],
                "randomforestregressor__min_samples_leaf": range(1, 5),
                "randomforestregressor__max_features": ["sqrt", "log2", None]
            }, "randomforestregressor__n_estimators"),
            "linear_svc":({
                "linearsvc__dual": [True, False],
                "linearsvc__C": [0.1, 1, 2, 5, 10]
            }, "n_samples"),
            "random_forest_classifier":({
                "randomforestclassifier__max_samples":[None, 0.3, 0.6],
                "randomforestclassifier__oob_score": [False, True],
                # "randomforestclassifier__n_estimators": [10, 50, 100, 250, 500],
                "randomforestclassifier__min_samples_leaf": range(1, 5)
            }, "randomforestclassifier__n_estimators"),
            "k_neighbors_classifier":({
                "kneighborsclassifier__n_neighbors": [1,5, 10],
                "kneighborsclassifier__weights": ["uniform", "distance"],
                "kneighborsclassifier__leaf_size":[15, 30, 45, 60]
            }, "n_samples")
        }

    def hyperparameter_optimize_single(self, model, model_name, X, y,
                                       cv: int = 3, scoring: str = "f1_weighted") -> object:
        n_samples = len(X)
        param_grid, resource = self.param_grids.get(model_name)
        if resource == "n_samples":
            max_resource = n_samples
            min_resource = n_samples//4
        elif "n_estimators" in resource:
            max_resource = 1000
            min_resource = 250

        model = HalvingRandomSearchCV(model, param_grid,
                                      resource=resource,
                                      min_resources=min_resource,
                                      max_resources=max_resource,
                                      factor=2,
                                      random_state=0,
                                      refit=True,
                                      n_jobs=-1,
                                      verbose=2,
                                      cv=cv).fit(X, y)

        # model = GridSearchCV(model, param_grid, cv=cv, verbose=2, refit=True).fit(X, y)

        return model
