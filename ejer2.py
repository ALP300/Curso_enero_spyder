# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 20:50:13 2025

@author: aitor
"""
import pandas as pd
import numpy as np
df = pd.read_csv('ATP.csv', encoding='latin-1')
print(df.head())
print(df.info())