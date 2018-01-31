#Remove highly correlated data

import matplotlib.pyplot as plt
import numpy as np
from six.moves import cPickle as pickle
import numpy as np

with open(r"../DataSet/CleanDataSet/dataset_voice.pickle", 'rb') as fl:
    data = pickle.load(fl)
    dataset = data['dataset']
    label = data['label']
    attributes =  data['attributes']

corrmat = np.corrcoef(dataset, rowvar=False)
corrmat = abs(corrmat)
print(corrmat)
matyes = corrmat>0.85
matyes =np.array(matyes)
print(matyes.shape)

ind = []
count = 0
for i in range(len(matyes)):
    if i not in ind:
        count += 1
        for j in range(i+1, len(matyes)):
            if corrmat[i][j] > 0.8:
                if j not in ind:
                    ind.append(j)
ind.sort()
arr = ind
deleted = []
count = 0
for i in range(len(arr)):
    deleted.append(attributes[0][arr[i]])
    count+=1
print(count)

for i in range(len(arr)):
    print(deleted[i], attributes[0][arr[i]-i])
    attributes[0].pop(arr[i] - i)
    dataset = np.delete(dataset, arr[i]-i, axis=1)
    dataset = np.delete(dataset, arr[i]-i, axis=1)
print(len(dataset[0]))
print(attributes)

print(count)

picklefile = r"../DataSet/CleanDataSet/varReduction2.pickle"
try:
    f = open(picklefile, 'wb')
    data = {
        'train_dataset': train_dataset,
        'train_labels': train_labels,
        'test_dataset': test_dataset,
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
    f.write("Remaininng columns : " + str(len(train_dataset[0])) + "\n")