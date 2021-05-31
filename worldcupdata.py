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

print(players.head())




matches = matches.set_index('Year')
names = matches[matches['Home Team Name'].str.contains('rn">')]['Home Team Name'].value_counts()
wrong = list(names.index)
correct = [name.split('>')[1] for name in wrong]
old_name = ['Germany FR', 'Maracan� - Est�dio Jornalista M�rio Filho', 'Estadio do Maracana']
new_name = ['Germany', 'Maracan Stadium', 'Maracan Stadium']
wrong = wrong + old_name
correct = correct + new_name
for index, wr in enumerate(wrong):
    cups = cups.replace(wrong[index], correct[index])
    
for index, wr in enumerate(wrong):
    matches = matches.replace(wrong[index], correct[index])
    
for index, wr in enumerate(wrong):
    players = players.replace(wrong[index], correct[index])
    
matches['Attendance'].fillna(method= 'ffill', inplace = True)
# Replace missing values or dropping duplicates
print(matches.isnull().sum())
print (matches.head())

# Slicing, loc or iloc.
home = matches[['Home Team Name', 'Home Team Goals']].dropna()
away = matches[['Away Team Name', 'Away Team Goals']].dropna()

home.columns = ['Countries', 'Goals']
away.columns = home.columns
goals = home.append(away, ignore_index = True)
goals = goals.groupby('Countries').sum()
goals = goals.sort_values(by = 'Goals', ascending=False)

# Looping, iterrows 


matches['Home Team Name'].value_counts()


print(cups.head())

names = matches[matches['Home Team Name'].str.contains('rn">')]['Home Team Name'].value_counts()

print(names)
winner = cups['Winner'].value_counts()
runnerup = cups['Runners-Up'].value_counts()
third = cups['Third'].value_counts()
print(winner)
print(runnerup)

# Merge DataFrames 
teams = pd.concat([winner, runnerup, third], axis=1)
teams.fillna(0, inplace=True)
teams = teams.astype(int)
print(teams)
sns.pairplot(teams)
cups['Attendance'] = cups['Attendance'].str.replace(".", "")
print(cups.head)
fig, ax = plt.subplots(figsize = (10,5))
sns.despine(right = True)
g = sns.barplot(x = 'Year', y = 'Attendance', data = cups)
g.set_xticklabels(g.get_xticklabels(), rotation = 80)
g.set_title('Attendance Per Year')
fig, ax = plt.subplots(figsize = (10,5))
sns.despine(right = True)
g = sns.barplot(x = 'Year', y = 'QualifiedTeams', data = cups)
g.set_xticklabels(g.get_xticklabels(), rotation = 80)
g.set_title('Qualified Teams Per Year')
fig, ax = plt.subplots(figsize = (10,5))
sns.despine(right = True)
g = sns.barplot(x = 'Year', y = 'GoalsScored', data = cups)
g.set_xticklabels(g.get_xticklabels(), rotation = 80)
g.set_title('Goals Scored by Teams Per Year')
fig, ax = plt.subplots(figsize = (10,5))
sns.despine(right = True)
g = sns.barplot(x = 'Year', y = 'MatchesPlayed', data = cups)
g.set_xticklabels(g.get_xticklabels(), rotation = 80)
g.set_title('Matches Played by Teams Per Year')
print(matches.head(2))
home = matches.groupby(['Year', 'Home Team Name'])['Home Team Goals'].sum()
away = matches.groupby(['Year', 'Away Team Name'])['Away Team Goals'].sum()
goals = pd.concat([home, away], axis=1)
goals.fillna(0, inplace=True)
goals['Goals'] = goals['Home Team Goals'] + goals['Away Team Goals']
goals = goals.drop(labels = ['Home Team Goals', 'Away Team Goals'], axis = 1)
goals = goals.reset_index()
goals.columns = ['Year', 'Country', 'Goals']
goals = goals.sort_values(by = ['Year', 'Goals'], ascending = [True, False])
top5 = goals.groupby('Year').head()

#  Define a custom function to create reusable code
def get_labels(matches):
    if matches['Home Team Goals'] > matches['Away Team Goals']:
        return 'Home Team Win'
    if matches['Home Team Goals'] < matches['Away Team Goals']:
        return 'Away Team Win'
    return 'DRAW'

matches['outcome'] = matches.apply(lambda x: get_labels(x), axis=1)
print(matches.head())
mt = matches['outcome'].value_counts()
plt.figure(figsize = (6,6))

mt.plot.pie(autopct = "%1.0f%%", colors = sns.color_palette('winter_r'), shadow = True)

c = plt.Circle((0,0), 0.4, color =  'white')
plt.gca().add_artist(c)
plt.title('Match Outcomes by Home and Away Teams')
plt.show()

