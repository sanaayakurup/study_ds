import pandas as pd
data=pd.read_csv('DataForLR.csv')
data.head()


import matplotlib.pyplot as plt 
data.plot(x='Hours',y='Score',kind='scatter')


#get x variable
Input=data.iloc[:, :-1].values #index all the rows, but remove last col 
Output=data.iloc[:,1].values


#SPLIT THE DATASET
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(Input,Output,train_size=0.7,random_state=1)
x_train.shape
x_test.shape
y_train.shape


from sklearn.linear_model import LinearRegression

lin_reg=LinearRegression()
lin_reg.fit(x_train,y_train)

y_pred=lin_reg.predict(x_test)

#evaluating the results 
#lets now see the mean absolute error 
from sklearn.metrics import mean_absolute_error,mean_squared_error
mean_absolute_error(y_test, y_pred)

#mean squared eror
print(mean_squared_error(y_test, y_pred))

#root mean squared error
from math import sqrt
print(sqrt(mean_squared_error(y_test, y_pred)))


#r squared 
from sklearn.metrics import r2_score
r2_score(y_test,y_pred)

#save model to the disk
import pickle 
pickle.dump(lin_reg,open('model.pkl','wb')) #write binary 


#loading model 
model=pickle.load(open('model.pkl','rb'))