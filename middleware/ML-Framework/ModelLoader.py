import pandas as pd
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor

class ModelLoader:
    def __init__(self, models=None, task="regression") -> None:
        """ 
        Creates ML models with the provided model names. 
        All models are supervised. They can either be regression or classification tasks.
        All model objects are stored in the ModelLoader().models_dict variable.

        Methods:
        ---
        .getAvailable() -> Returns all available model names for a given task (regression or classification)
        
        .load() -> loads all provided model names into the self._model_objects variable

        
        Parameters
        ---
        : models (list<str>): A list of model names. These models will be initilized. 
        The data can be fitted to all of them with the .fit() function.
        If no model names are provided all models for the selected task are created.
        
        : task (str) : The name of the task that should be performed. 
        Possible options are: regression and classification
        """
        # list of models that are available for loading
        self._available_models = {
            "regression": ["linear_regression", "sgd_regressor", "mlp_regressor", "random_forest_regressor"],
            "classification": []
            }
        self._task = task
        # model_dict will contain the name of the models as key and the model objects as values
        self.models_dict = {}
        self.load(models)
        

    def getAvailable(self, task):
        """Returns a list of the available ML models, that can be loaded via ModelLoader.load()"""
        try:
            avail = self._available_models[task]
            return avail
        except:
            print(f"Could not find {task}. Available options are: {self._available_models.keys()}")
            return
        

    def load(self, model_names=None, task=None):
        # reset previous model_dict to load new models
        self.models_dict = {}

        # override the previous task if a task is provided
        if task is not None:
            assert task in self._available_models.key(), "You have to select a valid task."
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

        # load all required ML models into the models_dict
        for name in self._model_names:
            if name in ["linear_regression", "linearregression"]:
                self.models_dict["linear_regression"] = LinearRegression()
            if name in ["sgd_regressor", "sgdregressor"]:
                self.models_dict["sgd_regressor"] = SGDRegressor()
            if name in ["mlp_regressor", "mlpregressor"]:
                self.models_dict["mlp_regressor"] = MLPRegressor()
            if name in ["random_forest_regressor", "randomforestregressor"]:
                self.models_dict["random_forest_regressor"] = RandomForestRegressor()


