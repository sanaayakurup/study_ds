# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 14:46:15 2022
https://www.youtube.com/watch?v=J73mvgG9fFs&list=PLKnIA16_RmvYXWH_E6PuVLLHHTWXwwDN7&index=12

@author: sanaayak
"""
import pandas as pd

url_data='https://raw.githubusercontent.com/campusx-official/100-days-of-machine-learning/main/day34-handling-date-and-time/messages.csv'
time = pd.read_csv(url_data)
time.head()
time.dtypes


url_data='https://raw.githubusercontent.com/campusx-official/100-days-of-machine-learning/main/day34-handling-date-and-time/orders.csv'
date_df=pd.read_csv(url_data)
date_df.head()


date_df.dtypes
#date is an object 


#all the date objects are stored as objects(strings)
#thus we must convert it to date_time ovjects 
time['date']=pd.to_datetime(time['date'])
time.dtypes

date_df['date']=pd.to_datetime(date_df['date'])
date_df.dtypes


#once converted to date, we can extract usefull info from the date 
#extract year 
date_df['year']=date_df['date'].dt.year
date_df['month']=date_df['date'].dt.month
date_df['Month']=date_df['date'].dt.month_name()

#get day 
date_df['day']=date_df['date'].dt.day

#get which dasy of the week 
date_df['day_of_week']=date_df['date'].dt.day_of_week

#get name of day of the week
date_df['ord_day_of_Week']=date_df['date'].dt.day_name()


#is the date a weekend?
date_df['is_weekend']=np.where(date_df['ord_day_of_Week'].isin(['Saturday', 'Sunday']),1,0)


#extract week of the year 
date['date_week']=date_df['date'].dt.isocalendar().week


#extract quarter 
date_df['qrtr']=date_df['date'].dt.quarter


#time
time.dtypes
time['date']=pd.to_datetime(time['date'])
time['sec']=time['date'].dt.second
time['minute']=time['date'].dt.minute
time['hour']=time['date'].dt.hour
time['date'].dt.time
