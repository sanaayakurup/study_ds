# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 12:12:02 2022
https://www.youtube.com/watch?v=xOccYkgRV4Q&list=PLKnIA16_RmvYXWH_E6PuVLLHHTWXwwDN7&index=7&t=79s

@author: sanaayak
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.compose import ColumnTransformer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn import set_config
set_config(display='diagram')

#Plan for pipeline 
#age and embarked need to be imputed for missing values using coltransformenr 
# sex and embarked need to be onehotencoded by coltrans
#scale all the x vars 
#featuer selection 
#train the data 

df=pd.read_csv('train.csv')
df.drop(columns=['PassengerId','Name','Ticket','Cabin'],axis=1,inplace=True)
X = df.drop('Survived', axis=1)
y = df['Survived']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state=42,stratify=y)
X_train.head()
X_train.shape
y_train.shape


#create a transformer to impute missing values for age
df.isnull().sum()
trf1 = ColumnTransformer([
    ('impute_age',SimpleImputer(),[2]),
    ('impute_embarked',SimpleImputer(strategy='most_frequent'),[6])
],remainder='passthrough')

# one hot encoding
trf2 = ColumnTransformer([
    ('ohe_sex_embarked',OneHotEncoder(sparse=False,handle_unknown='ignore'),[1,6])
],remainder='passthrough')

# Scaling
trf3 = ColumnTransformer([
    ('scale',MinMaxScaler(),slice(0,10))
])

# Feature selection
trf4 = SelectKBest(score_func=chi2,k=8)

#train model 
trf5=DecisionTreeClassifier()


#create pipeline 
pipe=make_pipeline(trf1,trf2,trf3,trf4,trf5)
pipe.fit(X_train,y_train)

#now the pipleine is trained 
y_pred=pipe.predict(X_test)

from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)

#cross validation using pipeline 
from sklearn.model_selection import cross_val_score
cross_val_score(pipe,X_train,y_train,cv=5,scoring='accuracy').mean()


# Gridsearc using pipeline
from sklearn.model_selection import GridSearchCV


params = {
    'trf5__max_depth':[1,2,3,4,5,None]
}


grid = GridSearchCV(pipe, params, cv=5, scoring='accuracy')
search = GridSearchCV(pipe, params)
grid.best_score_


# export 
import pickle
pickle.dump(pipe,open('pipe.pkl','wb'))
 