#converting data into array 

import numpy as np
import csv
from six.moves import cPickle as pickle

path = r'../DataSet/voice'

dataset = []
label = []
attributes = []

with open( path + ".csv", 'r') as p1:
    f1 = csv.reader(p1)
    count = 0
    for rows in f1:
      if count == 0 :
        attributes.append(rows[:-1])
        count=count+1
      else :
        dataset.append(rows[:-1])
        label.append(rows[-1])
    

path = r'../DataSet/dataset_voice.pickle'

dataset = np.array(dataset).astype(float)
label = np.array(label).astype(str)
attributes = np.array(attributes).astype(str)

try:
  f = open(path, 'wb')
  data = {
    'dataset': dataset,
    'label': label,
    'attributes': attributes
    }
  pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
  f.close()
except Exception as e:
  print('Unable to save data to', picklefile, ':', e)
  raise
