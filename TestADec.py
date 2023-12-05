from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
#from fffffff import DecisionTree
#from fasttrees import FastFrugalTreeClassifier
import pandas as pd
from sklearn import datasets, model_selection

from fasttrees import FastFrugalTreeClassifier
from sklearn.datasets import make_classification

# Load data set
iris_dict = datasets.load_iris(as_frame=True)

# Split into train and test data set
X_iris, y_iris = iris_dict['data'], iris_dict['target']
X_train_iris, X_test_iris, y_train_iris, y_test_iris = model_selection.train_test_split(
    X_iris, y_iris, test_size=0.4, random_state=42)

# Fit and test fitted tree
fftc = FastFrugalTreeClassifier()
fftc.fit(X_train_iris, y_train_iris)
fftc.score(X_test_iris, y_test_iris)

#from sklearn.tree import DecisionTreeClassifier
#from sklearn.metrics import confusion_matrix
#classifier = DecisionTreeClassifier()

#data = datasets.load_breast_cancer()
#X, y = data.data, data.target

#print(yq_train)
#ffdecisiontree = DecisionTreeClassifier()
#ffdecisiontree.fit(Xq_train, yq_train)

#ffqTree.fit(Xq_train, yq_train)


#prediction
#yq_pred = classifier.predict(Xq_test)#Accuracy
#cm = confusion_matrix(yq_test, yq_pred)
#print(cm)
