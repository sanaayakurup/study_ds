# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 17:38:31 2022
https://www.datacamp.com/tutorial/decision-tree-classification-python
@author: sanaayak
"""
import numpy as np
import pandas as pd 
import sklearn.datasets
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV

#LOADING SKLEARN DATA 
breast_cancer_dataset = sklearn.datasets.load_breast_cancer()
data_frame = pd.DataFrame(breast_cancer_dataset.data, columns = breast_cancer_dataset.feature_names)
data_frame.head()
data_frame['label'] = breast_cancer_dataset.target

data_frame['label'].value_counts()
X=data_frame.drop(columns='label',axis=1)
y=data_frame['label']

X=np.asarray(X)
Y=np.asarray(y)


#GRIDSEARCHCV -ALL COMBINATIONS OF hps ARE USED TO FIND 

#LOADING THE SVC MODEL
model=SVC()

#CREATE A DICT WITH hYPERPARAM VALUES 
parameters={
    'kernel':['linear','poly','rbf','sigmoid'],
    'C':[1,5,10,20]
    }
    
classifier=GridSearchCV(model, parameters, cv=5)   
classifier.fit(X,Y) 

#find the best paraeter-use this for the model to get best fit 
classifier.best_params_

    
#what is the highest accuracy 
highest_accuracy=classifier.best_score_

#result 
result =pd.DataFrame(classifier.cv_results_)


#RANDOMIZED SEARCH CV 
model=SVC()
parameters={
    'kernel':['linear','poly','rbf','sigmoid'],
    'C':[1,5,10,20]    
    
    }

classifier=RandomizedSearchCV(model,parameters,cv=5)
classifier.fit(X,Y)

classifier.best_params_
classifier.best_score_

#we then use the best params to train a model 
