import pandas as pd
import numpy as np
df = pd.read_csv(r'D:\Coding\mlintro\01_cleancode\vinoejemplo\winequality-red.csv', sep=';')
df.head()

#Funcion para calcular la calidad promedio de una metrica de vino (Alto y Bajo)
def calidad_promedio(mediana, datos, metrica):
    for i, columna in enumerate(datos):
        if columna >= mediana:
            df.loc[i, metrica] = 'alto'
        else:
            df.loc[i, metrica] = 'bajo'
    media = df.groupby(metrica).quality.mean()
    return print(media.to_string(),'\n')

