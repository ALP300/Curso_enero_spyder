# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 20:50:22 2025

@author: aitor
"""

import pandas as pd
df = pd.read_csv('ATP.csv', encoding='latin-1')
print(df.info())
print(df.head())
print("\n"*4)
print(df.iloc[0:21])
#REGLONES SALTEADOS
print(df.iloc[[0,3,6,24],])
#COLUMNAS
print(df.iloc[:,0:3])
print(df.iloc[[0,3,6,24],[0,5,6]])
print(df.iloc[[0,1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8,9]])
print("\n"*4)
print(df.iloc[0:8, 0:9])