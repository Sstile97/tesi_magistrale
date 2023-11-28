from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
from fffffff import DecisionTree
from fasttrees import FastFrugalTreeClassifier
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
classifier = DecisionTreeClassifier()

#data = datasets.load_breast_cancer()
#X, y = data.data, data.target
datas = pd.read_csv("penguins.csv")

cat_columns = ["Island", "Sex"]
for col in cat_columns:
    datas[col] = datas[col].astype('category')

nr_columns = ['Bill Length (mm)', 'Bill Depth (mm)', 'Flipper Length (mm)', 'Body Mass (g)', 'Year']
for col in nr_columns:
    # only recast columns that have not been correctly inferred
    if datas[col].dtype != 'float' and datas[col].dtype != 'int':
        # change the '?' placeholder to a nan
        datas.loc[datas[col] == '?', col] = np.nan
        datas[col] = datas[col].astype('float')

#True se la specie è Adelie, false se è qualsiasi altra specie
datas['Species'] = datas['Species'].apply(lambda x: True if x=='Adelie' else False).astype(bool)




X = datas.drop("Species", axis = 1)
y = datas["Species"]


column_types_X = X.dtypes
column_types_y = y.dtypes
#print(column_types_X)
#print("")
#print(column_types_y)
# iterating the columns
#for col in X.columns:
#print(X[1][1])
#print(y[0])
#print(X.head())
#print("")
#print(y.head())
#print("")
#print(datas.shape)


#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

X_train, X_test, y_train, y_test = train_test_split(datas.drop(columns='Species'), datas['Species'], test_size=0.33, random_state=0)


fftree = FastFrugalTreeClassifier()
#fftree.fit(X_train, y_train)







# Set a random seed for reproducibility
np.random.seed(42)

# Generate random data
dataq = {
    'Attribute1': np.random.randint(1, 100, size=100),
    'Attribute2': np.random.randint(50, 150, size=100),
    'Attribute3': np.random.randint(100, 200, size=100),
    'Target': np.random.choice([True, False], size=100)
}

# Create a DataFrame
dfq = pd.DataFrame(dataq)

# Display the first few rows of the DataFrame
#print(dfq.head())
Xq_train, Xq_test, yq_train, yq_test = train_test_split(dfq.drop(columns='Target'), dfq['Target'], test_size=0.33, random_state=0)
ffqTree = FastFrugalTreeClassifier()

print(yq_train)
ffdecisiontree = DecisionTreeClassifier()
#ffdecisiontree.fit(Xq_train, yq_train)

ffqTree.fit(Xq_train, yq_train)


#prediction
#yq_pred = classifier.predict(Xq_test)#Accuracy
#cm = confusion_matrix(yq_test, yq_pred)
#print(cm)
