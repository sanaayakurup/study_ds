# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 13:52:06 2022
https://colab.research.google.com/drive/1WoYOPLw_r5ju_kopma8iMKU9gmCDKIhm?usp=sharing
@author: sanaayak
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

# loading the csv data to a Pandas DataFrame
heart_data = pd.read_csv('heart.csv')
heart_data.head()

#1 is a defective heart, 0 is healthy 

heart_data.target
X=heart_data.drop(columns='target',axis=1)
Y=heart_data['target'].values


#train test split 
X_train,X_test, y_train, y_test=train_test_split(X,Y,test_size=0.2, stratify=Y, random_state=1)

X_train.shape
y_train.shape
X_test.shape
y_test.shape

#list of models- TO TEST which is the best model by comparing accuracy score 
models=[LogisticRegression(max_iter=1000),SVC(kernel='linear'),KNeighborsClassifier(),RandomForestClassifier()]

def compare_models_train_test():
    for model in models:
        model.fit(X_train,y_train)
        test_data_prediction=model.predict(X_test)
        accuracy=accuracy_score(y_test,test_data_prediction)
        print(f'accuracy of the {model} is {accuracy}')
        
compare_models_train_test()        

#if we change the random_state value-the accuracy will change 
#this is not reliable, thus we need CV 

###cROSS vALIDATION

#CV FOR LOGISTIC REG MODEL 
a=cross_val_score(LogisticRegression(max_iter=1000),X,Y,cv=5) #cv in this is stratified 
#each split will give us a sep accuracy-we can take the mean and get the total accuracy 
#this is more stable 
mean_accuracy_lr=np.mean(a)    


#similary for svc 
svc=cross_val_score(SVC(kernel='linear'),X,Y,cv=5)
mean_accuracy_svc=np.mean(svc)


for model in models:
    val=cross_val_score(model,X,Y,cv=5)
    print(f'{np.mean(val)} is the accuracy of {model}')