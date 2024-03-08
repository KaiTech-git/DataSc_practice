import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.model_selection import cross_val_score

data = pd.read_csv("/Users/admin/Desktop/Python/DataSc_practice/iris/iris.csv")

X = data[['SepalLengthCm','SepalWidthCm','PetalLengthCm']]
Y = data['Species']

model = svm.SVC()

accuracy = cross_val_score(model, X, Y, scoring='accuracy', cv = 10)
print(accuracy)
#get the mean of each fold 
print("Accuracy of Model with Cross Validation is:",accuracy.mean() * 100)