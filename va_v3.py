
import pandas as pd
df = pd.read_csv(r'D:\Coding\mlintro\01_cleancode\vinoejemplo\winequality-red-sp.csv', sep=';')
df.head()

mediana_alcohol = df.alcohol.median()
mediana_pH = df.pH.median()
mediana_azucarResidual = df.azucar_residual.median()
mediana_acidoCitrico = df.acido_citrico.median()

#Calidad de Alcohol en el vino
for i, alcohol in enumerate(df.alcohol):
    if alcohol >= mediana_alcohol:
        df.loc[i, 'alcohol'] = 'alto'
    else:
        df.loc[i, 'alcohol'] = 'bajo'
media_alcohol = df.groupby('alcohol').calidad.mean()
print(media_alcohol.to_string(),'\n')

#Calidad de pH en el vino
for i, pH in enumerate(df.pH):
    if pH >= mediana_pH:
        df.loc[i, 'pH'] = 'alto'
    else:
        df.loc[i, 'pH'] = 'bajo'
media_pH = df.groupby('pH').calidad.mean()
print(media_pH.to_string(),'\n')

#Calidad de Azucar Residual en el vino
for i, azucar_residual in enumerate(df.azucar_residual):
    if azucar_residual >= mediana_azucarResidual:
        df.loc[i, 'azucar residual'] = 'alto'
    else:
        df.loc[i, 'azucar residual'] = 'bajo'
media_azucarResidual = df.groupby('azucar residual').calidad.mean()
print(media_azucarResidual.to_string(),'\n')


#Calidad de Ácido Cítrico en el vino
for i, acido_citrico in enumerate(df.acido_citrico):
    if acido_citrico >= mediana_acidoCitrico:
        df.loc[i, 'acido citrico'] = 'alto'
    else:
        df.loc[i, 'acido citrico'] = 'bajo'
media_acidoCitrico = df.groupby('acido citrico').calidad.mean()
print(media_acidoCitrico.to_string(),'\n')


