import pandas as pd
import numpy as np
import math

#Ingreso de valores de 'x' y 'y'
x = float(input('Ingrese el valor de x: '))
y = float(input('Ingrese el valor de y: '))

#Menu de Operaciones
print('Seleccione la oepracion que desee realizar: ')
print('1. Suma')
print('2. Resta')
print('3. Multiplicacion')
print('4. Division')
print('5. Potencia')
print('6. Logaritmo (del primer numero [x])')

operacion = int(input('Cuál operación desea realizar? '))

#Calculo de Operaciones
if operacion == 1:
    resultado = x + y
    print('El resultado de ', x, ' mas ', y, 'es ', resultado)
elif operacion == 2:
    resultado = x - y
    print('El resultado de ', x, ' menos ', y, 'es ', resultado)
elif operacion == 3:
    resultado = x * y
    print('El resultado de ', x, ' por ', y, 'es ', resultado)
elif operacion == 4 and y!=0:
    resultado = x / y
    print('El resultado de ', x, ' entre ', y, 'es ', resultado)
elif operacion == 5:
    resultado == x**y
    print('El resultado de ', x, ' elevado a la ', y, 'es ', resultado)
elif operacion==6 and x>0:
    resultado = math.log10(x)
    print('El resultado del logaritmo de', x, 'es ', resultado)    
else:
    print('Elección no valida, vuelva a internatarlo.')

