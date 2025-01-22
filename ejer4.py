# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 21:38:39 2025

@author: aitor
"""

import pandas as pd
datos = pd.read_csv('ATP.csv', encoding='latin-1')
df= pd.DataFrame(datos)
df.reset_index().to_csv('DatosExportadosATP.csv',header=True, index=False)
datos.set_index('Location', inplace=True)
df= datos.loc['Melbourne']
df.reset_index().to_csv('MelbourneDatosATP.csv',header=True, index=False)

