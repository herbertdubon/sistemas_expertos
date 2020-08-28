
import pandas as pd
from funciones import calidad_promedio
df = pd.read_csv(r'D:\Coding\mlintro\01_cleancode\vinoejemplo\winequality-red-sp.csv', sep=';')
df.head()
#Calculo de medianas de metricas
mediana_alcohol = df.alcohol.median()
mediana_ph = df.pH.median()
mediana_azucarResidual = df.azucar_residual.median()
mediana_acidoCitrico = df.acido_citrico.median()

#Extraccion de datos de metricas
alcohol = df.alcohol
pH = df.pH
azucarResidual = df.azucar_residual
acidoCitrico = df.acido_citrico

#Calidad de Alcohol en el vino
calidad_promedio(mediana_alcohol, alcohol, 'alcohol')

#Calidad de pH en el vino
calidad_promedio(mediana_ph, pH, 'pH')

#Calidad de Azucar Residual en el vino
calidad_promedio(mediana_azucarResidual, azucarResidual, 'azucar_residual')

#Calidad de Ácido Cítrico en el vino
calidad_promedio(mediana_acidoCitrico, acidoCitrico, 'acido_citrico')

