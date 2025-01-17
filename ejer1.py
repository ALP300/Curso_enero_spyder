import pandas as pd
import numpy as np

datos= {'Nombre':['Leonardo','Joaquin','Alex','Paula','Enrique', 'Jhon'],
        'Materias':['Lenguaje','EDF','Química','Matemáticas','Inglés','Historia'],
        'Calificaciones':['18','20','13','19','16','17'],
        'Deportes':['Fútbol','Natación','Tenis','Voley','Natación','Balón Mano']
        }
df= pd.DataFrame(datos)
print(df)