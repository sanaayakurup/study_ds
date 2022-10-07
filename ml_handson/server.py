# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 18:28:48 2022

@author: sanaayak
"""
import numpy as np
from flask import Flask,request, jsonify
import pickle

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/api',methods=['POST'])
def predict():
    data=request.get_json() #fetches json data
    prediction=model.predict([[np.array(data['exp'])]])     # Make prediction using model loaded from disk as per the data.

    output=prediction[0]     # Take the first value of prediction

    return jsonify(output)


if __name__=='__main__':
    app.run(port=5000,debug=True)