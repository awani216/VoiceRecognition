import matplotlib.pyplot as plt
import numpy as np
from six.moves import cPickle as pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
import random

with open(r"../data_reduction_3.pickle", 'rb') as fl:
    data = pickle.load(fl)
    dataset = data['dataset']
    labels = data['labels']
    attributes =  data['attributes']
labels = np.array(labels, dtype=int)
clf = RandomForestClassifier()
#print(train_dataset.shape, train_labels.shape)
ran = random.sample(range(len(dataset)), 5000)
ran.sort()
print(ran)
clf.fit(dataset[ran], labels[ran])
importance = clf.feature_importances_
res = []
for i in range(len(importance)):
    res.append([importance[i], i])

res.sort()
arr = []
for i in range(len(res)):
    print("The importance of ", attributes[i], " is ", importance[i])
    if importance[i] <= 0.004:
        arr.append(i)
for  i in range(3):
    arr.append(i)
arr.sort()
deleted = []
count = 0
for i in range(len(arr)):
    deleted.append(attributes[arr[i]])
    count+=1
for i in range(len(arr)):
    print(deleted[i], attributes[arr[i]-i])
    attributes.pop(arr[i] - i)
    dataset = np.delete(dataset, arr[i]-i, axis=1)
    dataset = np.delete(dataset, arr[i]-i, axis=1)   

print(len(dataset[0]))
print(attributes)

print(count)

picklefile = r"..\random_forest.pickle"
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

path = "../reports/random_forest_reduction.txt"
with open(path, 'w') as f:
    f.write("Deleted columns in this step :" + str(len(deleted)) + "\n")
    for i in range(len(deleted)):
        f.write(deleted[i] + '\n')
    f.write("Remaininng columns : " + str(len(train_dataset[0])) + "\n")
