# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 15:42:47 2022

@author: sanaayak
"""
import pandas as pd

ser1=pd.Series([1,2,3],[3,4,5])
ser1 #the second list is the index value
#series always has one column 


print(ser1.iloc[2]) #integer location 2 pe what is there 
print(ser1[3]) # what is at loc 3-this functions as label loc 

dict(ser1) #can convert to dictionary 

s1=pd.Series([1,5,3,4],['a','b','c','d'])
s2=pd.Series([1,2,3,4],['a','b','c','d'])
s1+s2


s1.head(1)
s1.tail(2)

def mysquare(n):
    return n**n

mysquare(s1)
s1.apply(mysquare) #apply function applies a func on the whole series 

#sorting a series 
s1.sort_index()
s1.sort_values()
s1.sort_values(inplace=True)
s1


#pandas ploting func=v basic, need matplotlib
s1.plot()
s1.plot.pie()
s1.plot.hist()
s1.plot.bar()
s1.plot.barh()


s1.to_string()

#pandas dataframe
import matplotlib.pyplot as plt
data={
      'name':['anna','palla','pallas','snow'],
      'age':[1,2,3,4],
      'height':[2,3,4,5],
      'gender': ['m','m','f','f']
      }

pd_data=pd.DataFrame(data)
pd_data.set_index('name')

pd_data.head(2)
pd_data.tail(2)


#
pd_data.ndim #dimensions 
pd_data.shape #rows x cols 
pd_data.size #number of element 

pd_data.T

pd_data.plot()

#pandas statistical function
#count func
pd_data.count() #count for each 

#sum func
pd_data.height.sum()
pd_data.age.sum()

pd_data.age.prod() #product of all the ages 

#mean hegith 
pd_data.height.mean()

pd_data.height.median()
pd_data.height.mode() 
pd_data.height.std() #deviating from the mean 
pd_data.height.min()
pd_data.height.max()

pd_data.describe()
pd_data.info()


#itterrows by row
for key, items in pd_data.iterrows():
    print(items)
    
    
#iteritems-iterated by col    
for key, items in pd_data.iteritems():
            print(items)    