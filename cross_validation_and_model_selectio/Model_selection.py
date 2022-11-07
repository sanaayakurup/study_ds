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
from sklearn.model_selection import GridSearchCV

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
models = [LogisticRegression(max_iter=10000), SVC(), KNeighborsClassifier(), RandomForestClassifier(random_state=0)]
model_hyperparams={
    

    'log_reg_hyperparameters': {
        
        'C' : [1,5,10,20]
    },

    'svc_hyperparameters': {
        
        'kernel' : ['linear','poly','rbf','sigmoid'],
        'C' : [1,5,10,20]
    },


    'KNN_hyperparameters' : {
        
        'n_neighbors' : [3,5,10]
    },


    'random_forest_hyperparameters' : {
        
        'n_estimators' : [10, 20, 50, 100]
    }
}
    
type(model_hyperparams)    
model_hyperparams.keys()
model_hyperparams.values()
model_keys=list(model_hyperparams.keys())
model_hyperparams[model_keys[0]]


#def a model selection function with various hyperparams
def model_selection_hps(models,model_hyperparams):
    result=[]
    i=0
    for model in models:
        key=model_keys[i]
        params=model_hyperparams[key]
        i=i+1
        print(model)
        print(params)
        #now we have the model name and the model params 
        classifier=GridSearchCV(model,params,cv=5)
        classifier.fit(X,Y)
        result.append(
            {
            'model_use':key,
            'highest_score':classifier.best_score_,
            'best_param':classifier.best_params_
            }
            )
        result_df=pd.DataFrame(result,columns=['model_used','highest_score','best_param'])  
    return result_df

results=model_selection_hps(models,model_hyperparams)
