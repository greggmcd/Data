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
world_cups = '/Users/grefgg/Documents/Data/WorldCups.csv'
worldcup__df = pd.read_csv(world_cups)
worldcup_players_df = pd.read_csv(world_cup_players)
worldcup_matches_df = pd.read_csv(worldcup_data)

players = worldcup_players_df
matches = worldcup_matches_df
cups = worldcup__df

# Analysing data/ Cleaning data
print(players.head())
print(players.isnull().sum())
players = players.set_index('Team Initials')
players ["Position"].fillna(method = 'ffill',inplace= True)
players ["Event"].fillna(method = 'bfill',inplace= True)
players = players.drop_duplicates(subset= None, keep='first', inplace= False)
print(players.head())
print(players['Player Name'].describe())
players = players.drop_duplicates(['Coach Name','Event','Player Name'], keep='last')
players = players.groupby(['Team Initials','Event'])
print(players.head())


print(matches.head())

matches = matches.set_index('Year')
matches['Attendance'].fillna(method= 'ffill', inplace = True)
print(matches.isnull().sum())
print (matches.head())

total_goals = matches['Home Team Goals']+matches['Away Team Goals']
matches['Total Goals']= total_goals
matches.groupby(["Year"])["Total Goals"].sum()
print(matches.head())
sns.lineplot(data=matches, x="Year", y="Total Goals")
