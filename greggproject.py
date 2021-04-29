#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 16:46:38 2021

@author: grefgg
"""

import numpy as np
import pandas as pd
import requests

aus_weather = '/Users/grefgg/Desktop/weatherAUS.csv'
data = pd.read_csv(aus_weather)
data.head()
