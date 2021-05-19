#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 18 09:39:10 2021

@author: grefgg
"""

from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import requests
import json

#importing csv file world cup dataset from kaggle.
worldcup_data = '/Users/grefgg/Documents/Data/WorldCupMatches.csv'
worldcup_matches = pd.read_csv(worldcup_data)
print(worldcup_matches.head())
print(sns.pairplot(worldcup_matches))
sns.load_dataset("worldcup_data")
print(sns.heatmap(worldcup_matches.corr()))

