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

#importing csv file world cup dataset from kaggle and creating a dataframe.
worldcup_data = '/Users/grefgg/Documents/Data/WorldCupMatches.csv'
world_cup_players = '/Users/grefgg/Documents/Data/WorldCupPlayers.csv'
worldcup_matches_df = pd.read_csv(worldcup_data)
worldcup_matches_df = pd.read_csv(world_cup_players)

# Analysing data/ Cleaning data

print(worldcup_matches_df.head())
print(worldcup_matches_df.info())

# Replace missing values or dropping duplicates
print(worldcup_matches_df.isnull().sum())
print(worldcup_matches_df.head())

# Your project should include sorting, indexing, grouping.
new_index = worldcup_matches_df.set_index('RoundID')
new_index ["Position"].fillna(method = 'ffill',inplace= True)
new_index ["Event"].fillna(method = 'ffill',inplace= True)
new_index.drop_duplicates(subset= None, keep='first', inplace= False)
print (new_index.head())
teams = new_index.groupby('Team Initials')
coaches = new_index.groupby('Coach Name')
print(teams.first())
print(coaches.head())


# Slicing, loc or iloc.

# Looping, iterrows 
next(new_index.iterrows())[3:]

# Merge DataFrames 



#	Define a custom function to create reusable code. 