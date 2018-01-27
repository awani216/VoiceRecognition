import matplotlib.pyplot as plt
import numpy as np
from six.moves import cPickle as pickle
import numpy as np

with open(r"../DataSet/dataset_voice.pickle", 'rb') as fl:
    data = pickle.load(fl)
    dataset = data['dataset']
    label = data['label']
    attributes =  data['attributes']

path = r"../VARvsGEN/Normal_Data/plot_"
count = 0
for i in range(len(attributes[0])):
    if count != 0 :
        plt.clf()
        points = dataset[:,i]
        plt.plot(label, points, 'ro')
        plt.ylabel(attributes[0][i])
        plt.xlabel('Gender')
        plt.savefig(path+attributes[0][i]+".png")
        print("plotting graph " + str(i) + ": " + attributes[0][i])
    else:
        count=count+1
        print(count)
        continue
    # print("plotting graph " + str(i) + ": " + attributes[i])
