import pandas as pd
import numpy as np
import math


#Menu de Operaciones
while 1:
    print('Seleccione la oepracion que desee realizar: ')
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicacion')
    print('4. Division')
    print('5. Potencia')
    print('6. Logaritmo')

    operacion = int(input('\nCuál operación desea realizar?\n'))

    #Calculo de Suma
    if operacion == 1:
        x = float(input('Ingrese el valor de x: '))
        y = float(input('Ingrese el valor de y: '))
        resultado = x + y
        print('El resultado de {} mas {} es igual a {}'.format(x,y,resultado))
        menu = input('\nDesea realizar otra operación? (s/n)')
        if menu== "n":
            break
    
    #Calculo de Resta    
    elif operacion == 2:
        x = float(input('Ingrese el valor de x: '))
        y = float(input('Ingrese el valor de y: '))
        resultado = x - y
        print('El resultado de {} menos {} es igual a {}'.format(x,y,resultado))
        menu = input('\nDesea realizar otra operación? (s/n)')
        if menu== "n":
            break
    
    #Calculo de Multiplicación
    elif operacion == 3:
        x = float(input('Ingrese el valor de x: '))
        y = float(input('Ingrese el valor de y: '))
        resultado = x * y
        print('El resultado de {} multiplicado por {} es igual a {}'.format(x,y,resultado))
        menu = input('\nDesea realizar otra operación? (s/n)')
        if menu== "n":
            break
    
    #Calculo de División
    elif operacion == 4:
        x = float(input('Ingrese el valor de x: '))
        y = float(input('Ingrese el valor de y: '))
        if y==0:
            print('El valor de "y" no puede ser cero')
            menu = input('\nDesea realizar otra operación? (s/n)')
            if menu== "n":
                break
        else:
            resultado = x / y
            print('El resultado de {} dividido entre {} es igual a {}'.format(x,y,resultado))
            menu = input('\nDesea realizar otra operación? (s/n)')
            if menu== "n":
                break
    #Calculo de Potencia   
    elif operacion == 5:
        x = float(input('Ingrese el valor de x: '))
        y = float(input('Ingrese el valor de y: '))
        resultado = x**y
        print('El resultado de {} elevado a la {} es igual a {}'.format(x,y,resultado))
        menu = input('\nDesea realizar otra operación? (s/n)')
        if menu== "n":
            break
        
    #Calculo de Logaritmo    
    elif operacion==6:
        x = float(input('Ingrese el valor de x: '))
        if x <= 0:
            print('El valor de "x" no puede ser menor o igual a cero')
            menu = input('\nDesea realizar otra operación? (s/n)')
            if menu== "n":
                break
        else:
            resultado = math.log10(x)
            print('El resultado del logaritmo de {} es igual a {}'.format(x,resultado))
            menu = input('\nDesea realizar otra operación? (s/n)')
            if menu== "n":
                break        
    else:
        print('Elección no valida, vuelva a internatarlo.')

