
import pandas as pd
df = pd.read_csv(r'D:\Coding\mlintro\01_cleancode\vinoejemplo\winequality-red.csv', sep=';')
df.head()

mediana_alcohol = df.alcohol.median()
print(mediana_alcohol)
for i, alcohol in enumerate(df.alcohol):
    if alcohol >= mediana_alcohol:
        df.loc[i, 'alcohol'] = 'alto'
    else:
        df.loc[i, 'alcohol'] = 'bajo'
df.groupby('alcohol').quality.mean()
print(df.groupby('alcohol').quality.mean())

mediana_ph = df.pH.median()
print(mediana_ph)
for i, pH in enumerate(df.pH):
    if pH >= mediana_ph:
        df.loc[i, 'pH'] = 'alto'
    else:
        df.loc[i, 'pH'] = 'bajo'
df.groupby('pH').quality.mean()
print(df.groupby('pH').quality.mean())

mediana_azucarResidual = df.residual_sugar.median()
for i, residual_sugar in enumerate(df.residual_sugar):
    if residual_sugar >= mediana_azucarResidual:
        df.loc[i, 'residual sugar'] = 'alto'
    else:
        df.loc[i, 'residual sugar'] = 'bajo'
df.groupby('residual sugar').quality.mean()
print(df.groupby('residual sugar').quality.mean())

mediana_acidoCitrico = df.citric_acid.median()
for i, citric_acid in enumerate(df.citric_acid):
    if citric_acid >= mediana_acidoCitrico:
        df.loc[i, 'citric acid'] = 'alto'
    else:
        df.loc[i, 'citric acid'] = 'bajo'
df.groupby('citric acid').quality.mean()
print(df.groupby('citric acid').quality.mean())


