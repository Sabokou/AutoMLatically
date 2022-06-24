# script that will test if the ML code works

import sys
import os

####
# Importing from parent dir (https://www.geeksforgeeks.org/python-import-from-parent-directory/)
####
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
  
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
  
# adding the parent directory to 
# the sys.path.
sys.path.append(parent)
  
# now we can import the modules from the parent
# directory.
from ModelLoader import ModelLoader
from Preprocessing import Preprocessing

prepro = Preprocessing("./Salary_Data.csv")
lin_data = prepro.linear_preprocessing()
(X_train, X_test, y_train, y_test) = prepro.train_test_splitter(lin_data, y_name="Salary")
print("Linear Data:", lin_data)
print(f"---\n{X_train, X_test, y_train, y_test}")

loader = ModelLoader()
print(loader.models_dict)
loader.fit(X_train, y_train)
prediction_dict = loader.predict(X_test)
print(prediction_dict)
