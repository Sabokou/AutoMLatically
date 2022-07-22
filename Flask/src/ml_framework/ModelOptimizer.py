from typing import Dict
# explicitly require this experimental feature
from sklearn.experimental import enable_halving_search_cv # noqa
from sklearn.model_selection import HalvingRandomSearchCV


class ModelOptimizer:
    """
    This class is used to finetune models and optimize their hyperparameters.
    """

    def __init__(self):
        self.param_grids = {
            "linear_regression":{
                "linearregression__normalize":[True, False],
                "linearregression__positive": [True, False]
            },
            "sgd_regressor":{
                "sgdregressor__penalty": ["l2", "elasticnet"],
                "sgdregressor__alpha":[1e-3, 1e-4, 1e-5]
            },
            "mlp_regressor":{
                "mlpregressor__hidden_layer_sizes": [(100,), (50,), (150,)],
                "mlpregressor__alpha": [1e-3, 1e-4, 1e-5]
            },
            "random_forest_regressor":{
                "randomforestregressor__n_estimators": [10,50, 100, 250, 500],
                "randomforestregressor__min_samples_leaf": range(1, 5),
                "randomforestregressor__max_features": ["sqrt", "log2", None]
            },
            "linear_svc":{
                "linearsvc__dual": [True, False],
                "linearsvc__C": [0.1, 1, 2, 5, 10]
            },
            "random_forest_classifier":{
                "randomforestclassifier__max_samples":[None, 0.3, 0.6],
                "randomforestclassifier__oob_score": [False, True],
                "randomforestclassifier__n_estimators": [10, 50, 100, 250, 500],
                "randomfoestclassifier__min_samples_leaf": range(1, 5)
            },
            "k_neighbors_classifier":{
                "kneighborsclassifier__n_neighbors": [1,5, 10],
                "kneighborsclassifier__weights": ["uniform", "distance"],
                "kneighborsclassifier__leaf_size":[15, 30, 45, 60]
            }
        }



    def hyperparameter_optimize_single(self, model, model_name, X, y,
                                       cv: int = 5, scoring: str = "f1_weighted") -> object:

        param_grid = self.param_grids.get(model_name)

        model = HalvingRandomSearchCV(model, param_grid,
                                       resource='n_estimators',
                                       max_resources=10,
                                       random_state=0,
                                       refit=True).fit(X, y)

        return model
