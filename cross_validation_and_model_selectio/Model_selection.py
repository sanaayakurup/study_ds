# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 21:32:34 2022
https://www.youtube.com/watch?v=zU88wcLbBF8&t=572s

@author: Sanaaya
"""

import numpy as np
import pandas as pd
import seaborn as sns 

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

heart_data=pd.read_csv('heart.csv')
heart_data.head()
heart_data.target.value_counts()

#will a person have heart disease or not

X=heart_data.drop(columns='target',axis=1)
Y=heart_data.target

X=np.asarray(X)
Y=np.array(Y)

#Model Selection 
#comparing models with default hyperparms using cross val

#list of models
models=[LogisticRegression(max_iter=1000),SVC(kernel='linear'),KNeighborsClassifier(),RandomForestClassifier(random_state=10)]

#create a function that compares the accuracy score of these models
def compare_score():
    for model in models:
        cv_score=cross_val_score(model,X,Y,cv=5)
        print(f'{np.mean(cv_score)} for {model}')

compare_score()


##Comparing models with different hyperparam values
models=[LogisticRegression(max_iter=10000),SVC(),DecisionTreeClassifier(),KNeighborsClassifier(),RandomForestClassifier()]
model_hyperparams={
    'log_hps':{
        'C':[1,5,10,20]},
    'SVC_hps':{
        'kernel':['linear','poly','sigmoid','rbf']
        ,'C':[1,5,10,20]
        },
    'KNN_hps':{
        'n_neighbours':[3,5,10]
        },
    'RandomForest_hps':{
        'n_estimators':[10,20,50,100]
        }        
        }
    
type(model_hyperparams)    
model_hyperparams.keys()
model_hyperparams.values()
model_keys=list(model_hyperparams.keys())
