## removing data with low variance

import matplotlib.pyplot as plt
import numpy as np
from six.moves import cPickle as pickle
import numpy as np

with open(r"../DataSet/CleanDataSet/dataset_voice.pickle", 'rb') as fl:
    data = pickle.load(fl)
    dataset = data['dataset']
    label = data['label']
    attributes =  data['attributes']

mean = np.mean(abs(dataset), axis=0)
std = np.std(dataset, axis=0)
arr = []
for i in range(len(std)):
    if std[i] < 0.01:
        arr.append(i)
ind = np.array(arr, dtype=int)
deleted = []
count = 0

for i in range(len(arr)):
    deleted.append(attributes[arr[i]])
    count+=1

for i in range(len(arr)):
    print(deleted[i], attributes[arr[i]-i])
    attributes.pop(arr[i] - i)
    dataset = np.delete(dataset, arr[i]-i, axis=1)
    

print(count)

picklefile = r"../DataSet/CleanDataSet/varReduction1.pickle"
try:
  f = open(picklefile, 'wb')
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
path = "../Reports/varReduction1.txt"
with open(path, 'w') as f:
    f.write("Deleted columns in this step :" + str(len(deleted)) + "\n")
    for i in range(len(deleted)):
        f.write(deleted[i] + '\n')
    f.write("Remaininng columns : " + str(len(dataset[0])) + "\n")