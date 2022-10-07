# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 18:47:31 2022

@author: sanaayak
"""
#request.py is going to request the server for the predictions.

import requests
url = 'http://localhost:5000/api'

r = requests.post(url,json={'exp':1.8,})
print(r.json())
