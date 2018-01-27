import numpy as np
from numba import jit
import matplotlib.pyplot as plt
import time
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import svm
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from six.moves import cPickle as pickle
import random


with open(r"../DataSet/CleanDataSet/varReduction1.pickle", 'rb') as fl:
    data = pickle.load(fl)
    dataset = data['dataset']
    label = data['label']
    attributes =  data['attributes']

ran = np.random.permutation(len(dataset))
dataset = dataset[ran]
label = label[ran]
@jit
def func():    
    
    clf = ExtraTreesClassifier()
    ftime = time.time()
    clf.fit(dataset[:2100], label[:2100])
    ftime = time.time()
    x_test = dataset[-900:]
    y_test = label[-900:]
    res = clf.predict(x_test)
    ct = 0
    for i in range(len(res)):
        if res[i]==label[i] :
            ct=ct+1
            print("Time Taken ", time.time()-ftime)
    print("Accuracy in step " + str(100*(ct/len(res))))
    

func()