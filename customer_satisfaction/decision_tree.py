# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 10:55:54 2022
https://towardsdatascience.com/tree-based-algorithms-approach-on-predicting-customer-satisfaction-296730e19baa
@author: sanaayak
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report, accuracy_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV


# load the customer datasets
customer = pd.read_csv('./data/olist_customers_dataset.csv')
customer.head()

# load the order items datasets
order_items = pd.read_csv('./data/olist_order_items_dataset.csv')
order_items.head()

# load the order payments datasets
order_payments = pd.read_csv('./data/olist_order_payments_dataset.csv')
order_payments.head()


# load the order review datasets
order_reviews = pd.read_csv('./data/olist_order_reviews_dataset.csv')
order_reviews.head()

# load the orders datasets
orders = pd.read_csv('./data/olist_orders_dataset.csv')
orders.head()

# load the products datasets
products = pd.read_csv('./data/olist_products_dataset.csv')
products.head()

# load the sellers datasets
sellers = pd.read_csv('./data/olist_sellers_dataset.csv')
sellers.head()  

# load the product translation datasets
product_translation = pd.read_csv('./data/product_category_name_translation.csv')
product_translation.head()

#Merging all customer related datasets
A = pd.merge(orders,order_reviews,on='order_id')
A = pd.merge(A,order_payments,on='order_id')
A = pd.merge(A,customer,on='customer_id')
A.head()


#Merging all seller related datasets
B = pd.merge(order_items,products,on='product_id')
B = pd.merge(B,sellers,on='seller_id')
B = pd.merge(B,product_translation,on='product_category_name')
B.head()

#Merging customer and seller datasets
df_ecommerce = pd.merge(A,B, on = 'order_id')
df_ecommerce.head()
df_ecommerce.shape

#check for nulls as decision trees cannot process or handle missing data 
df_ecommerce.isnull().sum()


#Removing data with NaN value
prev_size = df_ecommerce.shape[0]
df_ecommerce.dropna(how='any',inplace=True)
df_ecommerce.isnull().sum()
current_size = df_ecommerce.shape[0]
print('From the data cleaning, we remove {}% of NaN value data'.format(round(((prev_size - current_size)/prev_size)*100,2)))



#Converting the timestamp format data to date data
time_stamp_cols=['order_purchase_timestamp',
       'order_approved_at', 'order_delivered_carrier_date',
       'order_delivered_customer_date', 'order_estimated_delivery_date','review_creation_date', 'review_answer_timestamp','shipping_limit_date']


#convert all the timestamps to date 
for i in time_stamp_cols:
    df_ecommerce[i]=pd.to_datetime(df_ecommerce[i]).dt.date
    
#Converting date time into string to remove the timestamp notation
df_ecommerce['delivery_days'] = df_ecommerce['order_delivered_customer_date'].sub(df_ecommerce['order_purchase_timestamp'],axis=0).astype(str)
df_ecommerce['estimated_days'] = df_ecommerce['order_estimated_delivery_date'].sub(df_ecommerce['order_purchase_timestamp'],axis=0).astype(str)
df_ecommerce['shipping_days'] = df_ecommerce['shipping_limit_date'].sub(df_ecommerce['order_purchase_timestamp'],axis=0).astype(str)

# Replacing the time stamp notation and converting type to int
df_ecommerce['delivery_days'] = df_ecommerce['delivery_days'].str.replace(" days","").astype(int)
df_ecommerce['estimated_days'] = df_ecommerce['estimated_days'].str.replace(" days","").astype(int)
df_ecommerce['shipping_days'] = df_ecommerce['shipping_days'].str.replace(" days","").astype(int)


df_ecommerce.drop(['order_purchase_timestamp', 'order_delivered_customer_date', 'order_estimated_delivery_date',
                   'shipping_limit_date'],axis=1,inplace=True)

#Result of data preprocessing
df_ecommerce.head()


#exploratory data analyisis
#what factors will influece customer satisfaction?
# -how fast the delivery was -delivey days, estimated vs sshipping days 
# -how fast the checkout was -
# -how good the returns were -no data 
# -how good the product was -review score

# What are the top ten most popular products among customers?
a=pd.DataFrame(df_ecommerce.groupby('product_id')['product_id'].count())
a.columns
df_ecommerce['product_category_name'].value_counts()[:10].plot(kind='bar')


#Set the bar chart
fig = plt.figure(figsize = (20,8))
ax = plt.axes() 
sns.barplot(x = df_ecommerce.product_category.value_counts().index[:10], 
            y = df_ecommerce.product_category.value_counts()[:10], ax = ax)
sns.set(font_scale = 1)

#Set the label name
ax.set_xlabel('Product category', fontsize = 16)
ax.set_ylabel('The quantity of order', fontsize = 16)

#Set the Suptitle
fig.suptitle("Top 10 best purchased product by customers", fontsize = 25)

plt.show()


#When it comes to paying the payment value, which payment method would the majority of customers prefer?
#coun the most used pyment value 
df_ecommerce['payment_type'].value_counts().sort_values().plot(kind='bar') #credit cars are used the most 

# How much will the payment value factor influence the customer review?
a=df_ecommerce.groupby(['payment_type','review_score'])['review_score'].count()


#feature engineering -adding some important features that will improve the model 
df_ecommerce['arrival_time'] = (df_ecommerce['estimated_days'] - df_ecommerce['delivery_days'])
#Creating new feature based on the arrival time of each order
delivery_arrival = []
d_arrival = df_ecommerce.arrival_time.values.tolist()

for i in d_arrival:
  if i <= 0:
    delivery_arrival.append('Late')
  else:
    delivery_arrival.append('On time')

df_ecommerce['delivery_arrival'] = delivery_arrival



#Creating new feature based on the review score of each order of good and bad review
df_ecommerce.loc[df_ecommerce['review_score'] < 3 ,'Score'] = 0
df_ecommerce.loc[df_ecommerce['review_score'] > 3,'Score'] = 1

#Removing review with value of 3 because it is a neutral review
df_ecommerce.drop(df_ecommerce[df_ecommerce['review_score'] == 3].index,inplace=True)
df_ecommerce.drop('review_score',axis=1,inplace=True)
print(df_ecommerce.shape)


#Label and one hot encoding process
#Handling column with 2 distinct value
df_ecommerce['order_status'] = df_ecommerce['order_status'].replace(['canceled','delivered'],[0,1])
df_ecommerce['delivery_arrival'] = df_ecommerce['delivery_arrival'].replace(['Late','On time'],[0,1])

#Handling column with more than 2 distinct value
one_hot_payment_type = pd.get_dummies(df_ecommerce['payment_type'])
df_ecommerce = df_ecommerce.join(one_hot_payment_type)

#Handling column with more than 10 distinct value
top_10_product_category = [x for x in df_ecommerce.product_category_name.value_counts().sort_values(ascending=False).head(10).index]

for label in top_10_product_category:
  df_ecommerce[label] = np.where(df_ecommerce['product_category_name']==label, 1,  0)
  
  #Droping any unimportant column for predicting process
df_ecommerce.drop(['payment_type','product_category_name'],axis=1,inplace=True)

df_ecommerce.head()
for i in df_ecommerce.columns:
    if df_ecommerce[i].dtypes==object:
        df_ecommerce.drop(columns=i,inplace=True)

#machine learning part 
# Split the data
X = df_ecommerce.drop(columns='Score').to_numpy()
y = df_ecommerce[['Score']].to_numpy()
y = y.reshape(len(y),) # sklearn's shape requirement

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

#Define Decision tree classifier model
dt_clf = DecisionTreeClassifier(random_state=42)

%%time
#Hyperparameter tuning
param = {'max_depth':  [1,2,3,4,5], 'min_samples_split': [5, 10, 100, 300,500,1000]}

#Grid search CV
dt_clf_gridcv = GridSearchCV(dt_clf,param,cv=3,refit=True,return_train_score=True,scoring='accuracy')
dt_clf_gridcv.fit(X_train,y_train)

#Results of GridSearchCV
cv_result = pd.DataFrame(dt_clf_gridcv.cv_results_)
retain_cols = ['params','mean_test_score','rank_test_score']
r=cv_result[retain_cols].sort_values('rank_test_score')

#Create confusion matrix
fig, ax = plt.subplots(figsize=(10,7))
sns.set(font_scale = 1.75)

y_test_pred = dt_clf_gridcv.best_estimator_.predict(X_test)
y_train_pred = dt_clf_gridcv.best_estimator_.predict(X_train)

cm = confusion_matrix(y_test, y_test_pred, labels = dt_clf_gridcv.best_estimator_.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix = cm,
                             display_labels = dt_clf_gridcv.best_estimator_.classes_)
disp.plot(ax = ax)
fig.suptitle('Decision tree confusion matrix', fontsize = 25)

plt.show()

#Evaluate decision tree model accuracy
accuracy_training = accuracy_score(y_train,y_train_pred)
accuracy_test = accuracy_score(y_test,y_test_pred)

print(f'Decision tree model')
print(f'Accuracy Training Data: {accuracy_training}')
print(f'Accuracy Test Data: {accuracy_test}')

#Classification report of previous model
print(f'Decision tree model')
print(classification_report(y_test, y_test_pred))