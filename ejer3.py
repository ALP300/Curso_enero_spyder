# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 21:07:23 2025

@author: aitor
"""

import pandas as pd
df = pd.read_csv('ATP.csv', encoding='latin-1')
print(df.info())
df.set_index('Location', inplace=True)
print("LOS DATOS DE Melbourne")
print(df.loc['Melbourne'])
print("\n"*4)
print("LOS DATOS DE ATLANTA EN SURFACE")
print("\n"*4)
print(df.loc['Atlanta','Surface'])
print("\n"*4)
print(df.loc[['Atlanta','Melbourne'],['Series','Court']])
print(df.loc[['Atlanta','Melbourne'], 'Series':'Round'])
print(df.loc[df['Series'].str.endswith('Slam')])
