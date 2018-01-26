# Removed few unwanted columns and replaced NaN with column mean

import pandas as pd
import numpy as np
import csv
from six.moves import cPickle as pickle

path = r"../DataSet/voice"
dest_path =  r"../DataSet/Clean DataSet/voice"

data = pd.read_csv(path+".csv")
data.fillna(data.mean())
data.to_csv(dest_path +".csv", encoding='utf-8')

path = r"../DataSet/voice.csv"
dest_path =  r"../DataSet/Clean DataSet/voice.csv"
data = pd.read_csv(path)
data.fillna(data.mean())
data.to_csv(dest_path, encoding='utf-8')

