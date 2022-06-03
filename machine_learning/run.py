import numpy as np
import pandas as pd
import scipy as sp
import sklearn as sk

# 1. receive the requested models for training
# 2. load the dataset from the frontened via async function
# 3. Preprocess the dataset based on the target feature (one-hot-encoding, ordinal encoding)
# 4. Train all selected models and save them on the server 
# 5. Send the performance of each model to the frontend
# 6. If the download of a model is requested, receive this request in the backend and download it to the client
