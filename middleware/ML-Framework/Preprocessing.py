import pandas as pd
import numpy as np
from sklearn.compose import make_column_selector
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import RobustScaler
from sklearn.compose import make_column_transformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OrdinalEncoder


class Preprocessing:
    def __init__(self):
        self.df = pd.read_csv("../public/datafile.csv")

    def linear_preprocessing(self):
        linear_processor_categorical = OneHotEncoder(handle_unknown="ignore")
        linear_processor_numerical = make_pipeline(
            RobustScaler(), SimpleImputer(strategy="mean", add_indicator=True)
        )

        linear_preprocessor = make_column_transformer(
            (linear_processor_numerical, make_column_selector(dtype_include=np.number)), (linear_processor_categorical, make_column_selector(dtype_include=object))
        )

        LP_df = linear_preprocessor.fit_transform(self.df)
        return LP_df

    def tree_preprocessing(self):
        tree_processor_categorical = OrdinalEncoder(
            handle_unknown="use_encoded_value", unknown_value=-1
        )
        tree_processor_numerical = SimpleImputer(strategy="mean", add_indicator=True)

        tree_preprocessor = make_column_transformer(
            (tree_processor_numerical, make_column_selector(dtype_include=np.number)), (tree_processor_categorical, make_column_selector(dtype_include=object))
        )

        TP_df = tree_preprocessor.fit_transform(self.df)
        return(TP_df)

if __name__=="__main__":

    new_prep = Preprocessing()
    print(new_prep.df)

    LP = new_prep.linear_preprocessing()
    print(LP)

    TP = new_prep.tree_preprocessing()
    print(TP)
