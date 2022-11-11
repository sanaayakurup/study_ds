# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 16:00:47 2022
https://www.youtube.com/watch?v=9ffkBvh8PTQ

@author: Sanaaya
"""

import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import r2_score


gold_data=pd.read_csv('./data/gld_price_data.csv')

gold_data.describe()
gold_data.info()
gold_data.head()
gold_data.tail()
gold_data.shape

#we need to predict the GLD var 
# USO is oil price

#basic info about the data 
gold_data.info()
gold_data.isnull().sum() #no missing values 
gold_data.isna().sum() #no nas 

##statistical measures of the data 
gold_data.describe()


#positive and negative corrs
corr_data=gold_data.corr()
sns.heatmap(corr_data,cmap='Blues')

#high positive corr with SLV, slight negative with USO 
corr_data['GLD']


#DISTRIBUTION OF GLD 
sns.distplot(gold_data['GLD'])

#now we split train and test data 
X=gold_data.drop(columns=['GLD','Date'],axis=1)
y=gold_data['GLD']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=20)


#model training -random forest regressor 
model=RandomForestRegressor(n_estimators=100)
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

r2_score(y_test, y_pred) #good score as the values are high but r2 is low 

#predict actual vs pred
y_test=np.array(y_test)

plt.plot(y_test,color='blue',label='actual_value')
plt.plot(y_pred,color='green',label='pred')


#check if other models perform better for this
 #linear reg, svc, dt-HW 
 