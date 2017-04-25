import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas.tools.plotting import parallel_coordinates

import sys
sys.path.append('../')
import preprocess

filename = '../data/train.csv'

dataset = preprocess.transform(filename)
X = dataset['data']
X = X[['Gender','Income','HouseholdStatus','EducationLevel','Party']]
y = dataset['target']

total = ((pd.concat([X, y], axis=1)).dropna())[:100]

mapping = {1:'happy', 0:'unhappy'}
total = total.replace({'Happy': mapping})

plt.figure()
parallel_coordinates(total, 'Happy', color = ['red','blue'])
plt.title("Parallel Coordinates Plot")
plt.xlabel("Five dimensions")
plt.ylabel("The discrete numbers of the categories")
plt.show()