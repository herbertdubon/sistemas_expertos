
import pandas as pd
df = pd.read_csv(r'D:\Coding\mlintro\01_cleancode\vinoejemplo\winequality-red.csv', sep=';')
df.head()

mediana_alcohol = df.alcohol.median()
mediana_pH = df.pH.median()
mediana_azucarResidual = df.residual_sugar.median()
mediana_acidoCitrico = df.citric_acid.median()

#Calidad de Alcohol en el vino
for i, alcohol in enumerate(df.alcohol):
    if alcohol >= mediana_alcohol:
        df.loc[i, 'alcohol'] = 'alto'
    else:
        df.loc[i, 'alcohol'] = 'bajo'
media_alcohol = df.groupby('alcohol').quality.mean()
print(media_alcohol.to_string(),'\n')

#Calidad de pH en el vino
for i, pH in enumerate(df.pH):
    if pH >= mediana_pH:
        df.loc[i, 'pH'] = 'alto'
    else:
        df.loc[i, 'pH'] = 'bajo'
media_pH = df.groupby('pH').quality.mean()
print(media_pH.to_string(),'\n')

#Calidad de Azucar Residual en el vino
for i, residual_sugar in enumerate(df.residual_sugar):
    if residual_sugar >= mediana_azucarResidual:
        df.loc[i, 'residual sugar'] = 'alto'
    else:
        df.loc[i, 'residual sugar'] = 'bajo'
media_azucarResidual = df.groupby('residual sugar').quality.mean()
print(media_azucarResidual.to_string(),'\n')


#Calidad de Ácido Cítrico en el vino
for i, citric_acid in enumerate(df.citric_acid):
    if citric_acid >= mediana_acidoCitrico:
        df.loc[i, 'citric acid'] = 'alto'
    else:
        df.loc[i, 'citric acid'] = 'bajo'
media_acidoCitrico = df.groupby('citric acid').quality.mean()
print(media_acidoCitrico.to_string(),'\n')


