#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 16:46:38 2021

@author: grefgg
"""

import numpy as np
import pandas as pd
import requests
import json
import matplotlib.pyplot as plt
import seaborn as sns
aus_weather = '/Users/grefgg/Desktop/weatherAUS.csv'
data_test= pd.read_csv(aus_weather)
data_test.head()
print(data_test.shape)
missing_values = data_test.isnull().sum()
print (missing_values)
print(data_test.columns)
print(data_test.describe())
print(data_test.values)
print(data_test.plot.line(y='Sunshine'))
print(sns.pairplot(data_test))
print(data_test['Rainfall'].mean())
