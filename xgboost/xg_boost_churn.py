# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 13:52:19 2022
https://www.youtube.com/watch?v=GrJP9FLV3FE
@author: sanaayak
predict is someone is going to stop using telco service i.e. customer churn
"""

import pandas as pd
import numpy as np

df=pd.read_excel('./data/Telco_customer_churn.xlsx')
df.drop(columns=['Churn Label','Churn Score', 'CLTV', 'Churn Reason'],axis=1,inplace=True)

#some columns with single values
df.Count.value_counts() #quite useless
df.Country.value_counts()
df.State.value_counts()
df.City.value_counts()

df.drop(columns=['CustomerID','Count','Country', 'State','Lat Long'],axis=1, inplace=True)

df.City.replace(' ','_',regex=True,inplace=True) #removing whitespaces

df.columns=df.columns.str.replace(' ','_')
df.head()





#Missing data
df.isna().sum()
df.isnull().sum()
df.dtypes

#verify each of the coluns
df.City.unique()
df.Phone_Service.unique()
df.Total_Charges.unique()

df[df['Total_Charges']==' '] #blank values
df.loc[df['Total_Charges']==' ','Total_Charges']=0 #blank values removed
len(df[df['Total_Charges']==' '])

df['Total_Charges']=pd.to_numeric(df['Total_Charges'])


df.replace(' ','_',regex=True,inplace=True) #replace all blanks

df.head()


#Format data-split into x and y

X=df.drop('Churn_Value',axis=1)
y=df.Churn_Value


#one hot encoding
objectcols=[]
for i in df.columns:
  if df[i].dtypes=='object':

    objectcols.append(i)


X_encoded=pd.get_dummies(X, columns=objectcols)
X_encoded.head(6)

y.value_counts()

#formatting done
#split into train and test with stratify as the unbalanced data is a problem
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X_encoded,y,test_size=0.2, stratify=y)

sum(y_train/len(y_train))
sum(y_test/len(y_test))

#train and test both have same split of classe
import xgboost as xgb
from sklearn.metrics import balanced_accuracy_score, roc_auc_score,make_scorer
clf_xgb=xgb.XGBClassifier(objective='binary:logistic',missing=None,seed=42)
clg_