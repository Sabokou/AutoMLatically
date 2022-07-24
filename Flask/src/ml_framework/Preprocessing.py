import pandas as pd
import numpy as np
from sklearn.compose import make_column_selector
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import RobustScaler
from sklearn.compose import make_column_transformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split


class Preprocessing:
    def __init__(self, data_path=None):
        self.df = None
        if data_path is not None:
            self.read_csv(data_path)

    def read_csv(self, data_path):
        self.df = pd.read_csv(data_path)

    @staticmethod
    def train_test_splitter(df, y_name: str, test_size: float =0.2):
        """
        Takes in the dataframe that should be transformed, the column name that is considered the gold label in the training process.
        The size for the train test split in percent can optionally be set to other values besides 80/20 train/test split.
        """
        columns = [col for col in df]
        assert y_name in columns, f"The label column '{y_name}' is not in the dataframe columns: {columns}"
        assert type(test_size) == float, f"Please provide a float value between 0 and 1. You provided: {test_size}"

        labels = df[y_name]

        X_train, X_test, y_train, y_test = train_test_split(df.drop(y_name, axis="columns", inplace=False),
                                                            labels, test_size=test_size)

        return X_train, X_test, y_train, y_test

    @staticmethod
    def linear_preprocessing():
        linear_processor_categorical = OneHotEncoder(handle_unknown="ignore")
        linear_processor_numerical = make_pipeline(
            RobustScaler(),
            SimpleImputer(strategy="mean", add_indicator=True)
        )

        linear_preprocessor = make_column_transformer(
            (linear_processor_numerical, make_column_selector(dtype_include=np.number)),
            (linear_processor_categorical, make_column_selector(dtype_include=object)),
            verbose_feature_names_out=False  # don't use a prefix that shows the transformations of the column
        )
        return linear_preprocessor

        # keep the transformed data as a df. See: https://stackoverflow.com/questions/68874492/preserve-column-order-after-applying-sklearn-compose-columntransformer/70526434#70526434
        # LP_df = pd.DataFrame(linear_preprocessor.fit_transform(self.df), columns=linear_preprocessor.get_feature_names_out())
        # return LP_df

    @staticmethod
    def tree_preprocessing():
        tree_processor_categorical = OrdinalEncoder(
            handle_unknown="use_encoded_value", unknown_value=-1
        )
        tree_processor_numerical = SimpleImputer(strategy="mean", add_indicator=True)

        tree_preprocessor = make_column_transformer(
            (tree_processor_numerical, make_column_selector(dtype_include=np.number)),
            (tree_processor_categorical, make_column_selector(dtype_include=object)),
            verbose_feature_names_out=False
        )

        return tree_preprocessor

        # TP_df = pd.DataFrame(tree_preprocessor.fit_transform(self.df), columns=tree_preprocessor.get_feature_names_out())
        # return(TP_df)


if __name__ == "__main__":
    new_prep = Preprocessing()
    print(new_prep.df)

    LP = new_prep.linear_preprocessing()
    print(LP)

    TP = new_prep.tree_preprocessing()
    print(TP)
