import pandas as pd
import numpy as np
df = pd.read_csv(r'D:\Coding\mlintro\01_cleancode\vinoejemplo\winequality-red.csv', sep=';')
df.head()

media_alcohol = df.alcohol.median()
media_ph = df.pH.median()
media_azucarResidual = df.residual_sugar.median()
media_acidoCitrico = df.citric_acid.median()

metrica = "alcohol"
array = np.array(metrica)


def calidad_promedio(mediana, array):
    for i, array in enumerate(df.array):
        if array >= mediana:
            df.loc[i, array] = 'alto'
        else:
            df.loc[i, array] = 'bajo'
    df.groupby(array).quality.mean()
    print(df.groupby(array).quality.mean())


calidad_promedio(media_alcohol, array)
print(calidad_promedio)


# metrica = 'pH'
# item = 'pH'
# calidad_promedio(item, metrica)
# print(calidad_promedio)