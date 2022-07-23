import numpy as np

# regression
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor

# classification
from sklearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

# Pipeline builder
from ml_framework.Preprocessing import Preprocessing


class ModelLoader:
    def __init__(self, models=None, task="regression") -> None:
        """ 
        Creates ML models with the provided model names. 
        All models are supervised. They can either be regression or classification tasks.
        All model objects are stored in the ModelLoader().models_dict variable.
        If the predict method was called with the optional y parameter, the self.mae and self.best_model variables are accessable.

        Methods:
        ---
        .get_available() -> Returns all available model names for a given task (regression or classification)
        
        .load() -> loads all provided model names into the self._model_objects variable

        .fit() -> fits the provided training data to all loaded models

        .predict() -> uses all loaded models to make predictions; An optional "y" parameter is used to measure the performance of the prediction.
        
        Parameters
        ---
        : models (list<str>): A list of model names. These models will be initilized. 
        The data can be fitted to all of them with the .fit() function.
        If no model names are provided all models for the selected task are created.
        
        : task (str) : The name of the task that should be performed. 
        Possible options are: regression and classification
        """
        self.best_model = None
        self.pipeline_builder = Preprocessing()

        # list of models that are available for loading
        self._available_models = {
            "regression": ["linear_regression", "sgd_regressor", "mlp_regressor", "random_forest_regressor"],
            "classification": ["linear_svc", "random_forest_classifier", "k_neighbors_classifier"]
        }
        self._task = task
        # model_dict will contain the name of the models as key and the model objects as values
        self.models_dict = {}
        # contains the mean absolut error if it should be calculated during model prediction
        self.mae = {}
        self.load(models)

    def get_available(self, task: str = None):
        """
        Returns a list of the available ML models, that can be loaded via ModelLoader.load()
        The structure is:
        {"classification": [<list of classification model names>],
        "regression": [<list of regression model names>]}

        If you provide a task (classification/regression) only a list of the available models in that task are returned.
        """
        if task is None:
            return self._available_models
        try:
            avail = self._available_models[task]
            return avail
        except:
            print(f"Could not find {task}. Available options are: {self._available_models.keys()}")
            return

    def load(self, model_names=None, task=None) -> None:
        # reset previous model_dict to load new models
        self.models_dict = {}

        # override the previous task if a task is provided
        if task is not None:
            assert task in self._available_models.keys(), "You have to select a valid task."
            self._task = task

        # initilize the provided models or intilize all models if none are provided
        if model_names is not None:
            try:
                self._model_names = [m.lower() for m in model_names]
            except:
                print(f"The provided models: {model_names} are not formatted as strings")
        else:
            # use all models for the selected task
            self._model_names = self._available_models[self._task]

        # get preprocessing variations
        linear_preprocessor = Preprocessing.linear_preprocessing()
        tree_preprocessor = Preprocessing.tree_preprocessing()

        # load all required ML models into the models_dict
        for name in self._model_names:
            # regression
            if name in ["linear_regression", "linearregression"]:
                self.models_dict["linear_regression"] = make_pipeline(
                    linear_preprocessor, LinearRegression())
            if name in ["sgd_regressor", "sgdregressor"]:
                self.models_dict["sgd_regressor"] = make_pipeline(
                   linear_preprocessor, SGDRegressor())
            if name in ["mlp_regressor", "mlpregressor"]:
                self.models_dict["mlp_regressor"] = make_pipeline(
                   linear_preprocessor, MLPRegressor())
            if name in ["random_forest_regressor", "randomforestregressor"]:
                self.models_dict["random_forest_regressor"] = make_pipeline(
                   tree_preprocessor, RandomForestRegressor())
            # classification
            if name in ["linear_svc", "linearsvc"]:  # linear support vector classification
                self.models_dict["linear_svc"] = make_pipeline(linear_preprocessor, LinearSVC())
            if name in ["random_forest_classifier", "randomforestclassifier"]:
                self.models_dict["random_forest_classifier"] = make_pipeline(
                   tree_preprocessor, RandomForestClassifier())
            if name in ["k_neighbors_classifier", "kneighborsclassifier"]:
                self.models_dict["k_neighbors_classifier"] = make_pipeline(
                   linear_preprocessor, KNeighborsClassifier())

    def fit(self, X, y) -> None:
        """Fit the training data X and the respective gold labels y to train all selected models in the ModelLoader."""
        for model in self.models_dict:
            self.models_dict[model] = self.models_dict[model].fit(X, y)

    @staticmethod
    # @np.vectorize
    def _calc_mae(y, pred):
        y, pred = np.array(y), np.array(pred)
        abs = np.abs(y - pred)
        mean = np.mean(abs)
        return mean

    def select_best_model(self) -> None:
        """Reads the self.mae dict and stores the model with the lowest score to self.best_model."""
        currently_best_model = None
        currently_best_perf = np.inf

        for item in self.mae.items():
            print("This is the item",item)
            # item tuple = (model_name, model_performance)
            if item[1] < currently_best_perf:
                currently_best_perf = item[1]
                currently_best_model = item[0]

        self.best_model = {currently_best_model:self.models_dict[currently_best_model]}

    def predict(self, X, y=None) -> dict:
        """Use all loaded models in the ModelLoader to make predictions for the test data X.
        If y is provided, the mean absolute error is calculated between the predictions and the gold label y.

        Returns:
        ---
        : predictions (dict) : Dictionary with the model names as keys and respective predictions as values 
        """
        # initialize a dictionary with the model names and an empty list that is filled with the predictions
        predictions = {}
        for model in self.models_dict:
            predictions[model] = self.models_dict[model].predict(X)

        if y is not None:
            for model, prediction in predictions.items():
                mean = self._calc_mae(y, prediction)
                print(f"In predict: {model} has mean of {mean}")
                self.mae[model] = mean
            self.select_best_model()

        return predictions
