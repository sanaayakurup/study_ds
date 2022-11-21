# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 20:09:16 2022

@author: Sanaaya
"""

from sklearn.ensemble import AdaBoostClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics 
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold


#adaboost for classification

from sklearn.datasets import make_classification
X,y=make_classification(n_samples=1000,n_features=20,n_informative=15,n_redundant=5,random_state=1)
#summarise the ds
X.shape
y.shape


#we have x and y, we can do cv 
model=AdaBoostClassifier()
cv=RepeatedStratifiedKFold(n_splits=10,n_repeats=3,random_state=1)
n_scores = cross_val_score(model, X, y, scoring='accuracy', cv=cv, n_jobs=-1, error_score='raise')

# report performance
print('Accuracy: %.3f (%.3f)' % (np.mean(n_scores), np.std(n_scores)))


#now we know the accuracy, we can use adaboost
model=AdaBoostClassifier()
model.fit(X,y)

# make a single prediction
row = [[-3.47224758,1.95378146,0.04875169,-0.91592588,-3.54022468,1.96405547,-7.72564954,-2.64787168,-1.81726906,-1.67104974,2.33762043,-4.30273117,0.4839841,-1.28253034,-10.6704077,-0.7641103,-3.58493721,2.07283886,0.08385173,0.91461126]]
yhat = model.predict(row)
print('Predicted Class: %d' % yhat[0])



##adaboost for regression
