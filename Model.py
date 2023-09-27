#importing required libraries

import warnings

import metrics
import pandas as pd
from sklearn import metrics
from feature import FeatureExtraction
warnings.filterwarnings('ignore')
import pickle

#Loading data into dataframe

data = pd.read_csv("Data/5.urldata.csv")
data.head()

data = data.drop('Domain', axis=1)

# Splitting the dataset into dependant and independant fetature

X = data.drop(["Label"],axis=1)
y = data["Label"]

# Splitting the dataset into train and test sets: 80-20 split

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
var = X_train.shape, y_train.shape, X_test.shape, y_test.shape

# Creating holders to store the model performance results
ML_Model = []
accuracy = []
f1_score = []
recall = []
precision = []

#function to call for storing the results
def storeResults(model, a,b,c,d):
  ML_Model.append(model)
  accuracy.append(round(a, 3))
  f1_score.append(round(b, 3))
  recall.append(round(c, 3))
  precision.append(round(d, 3))


# Decision Tree Classifier model
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100,max_features='sqrt')
model.fit(X_train,y_train)

#predicting the target value from the model for the samples

y_train_tree = model.predict(X_train)
y_test_tree = model.predict(X_test)

#computing the accuracy, f1_score, Recall, precision of the model performance

file = open('stat.txt', 'w')

acc_train_tree = metrics.accuracy_score(y_train,y_train_tree)
acc_test_tree = metrics.accuracy_score(y_test,y_test_tree)
file.write("Decision Tree : Accuracy on training Data: {:.3f}".format(acc_train_tree))
file.write("\nDecision Tree : Accuracy on test Data: {:.3f}".format(acc_test_tree))
file.write("\n\n")

f1_score_train_tree = metrics.f1_score(y_train,y_train_tree)
f1_score_test_tree = metrics.f1_score(y_test,y_test_tree)
file.write("\nDecision Tree : f1_score on training Data: {:.3f}".format(f1_score_train_tree))
file.write("\nDecision Tree : f1_score on test Data: {:.3f}".format(f1_score_test_tree))
file.write("\n")

recall_score_train_tree = metrics.recall_score(y_train,y_train_tree)
recall_score_test_tree = metrics.recall_score(y_test,y_test_tree)
file.write("\nDecision Tree : Recall on training Data: {:.3f}".format(recall_score_train_tree))
file.write("\nDecision Tree : Recall on test Data: {:.3f}".format(recall_score_test_tree))
file.write("\n")

precision_score_train_tree = metrics.precision_score(y_train,y_train_tree)
precision_score_test_tree = metrics.precision_score(y_test,y_test_tree)
file.write("\nDecision Tree : precision on training Data: {:.3f}".format(precision_score_train_tree))
file.write("\nDecision Tree : precision on test Data: {:.3f}".format(precision_score_test_tree))

pickle.dump(model, open('model.pkl', 'wb'))