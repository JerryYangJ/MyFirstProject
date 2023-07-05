"""
@author: JerryYang
@file: test.py
@time: 2023/6/15 17:26
@desc:
"""
from sklearn import datasets
import numpy as np
iris =datasets.load_iris()
X = iris.data[:,[2,3]]
Y = iris.target
print(np.unique(Y))