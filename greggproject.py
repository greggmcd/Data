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
data_test.corr()
print(sns.heatmap(data_test.corr()))


print(worldcup_matches_df.head())
print(worldcup_matches_df.info())
players = pd.read_csv(world_cup_players)
print(players.head())
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
print(teams.head())
print(coaches.head())


# Slicing, loc or iloc.
team_event_df = new_index.iloc[3::6]
print(team_event_df.head())
# Looping, iterrows 
next(new_index.iterrows())[3:6]
print(matches['Home Team Name'].value_counts())

# Merge DataFrames 
