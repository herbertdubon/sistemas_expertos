import math
import cmath

while 1:
# Menu de seleccion 
    print("CALCULADORA")
    print("Debe elegir una opción")
    print("1-Suma")
    print("2-Resta")
    print("3-Multiplicación")
    print("4-División")
    print("5-Raiz Cuadrada")
    print("6-Convertir Grados a Radianes")
    print("7-Factorial de un Número")
    print("8-Hipotenusa de un Triangulo")
    x= input("Escribe tu elección:\n")
    y=float(x)
    # Suma
    if(y==1):
        a=float(input("Ingresa un número\n"))
        b=float(input("Ingresa otro número\n"))
        print("La suma es:",a+b)
        operar = input("¿quiere seguir operando? (s/n)")
        if operar== "n":
            break
    #Resta
    elif(y==2):
        a=float(input("Ingresa un número\n"))
        b=float(input("Ingresa otro número\n"))
        print("El resultado de la resta es:",a-b)
        operar = input("¿quiere seguir operando? (s/n)")
        if operar== "n":
            break
    #Multiplicación         
    elif(y==3):
        a=float(input("Ingresa un número\n"))
        b=float(input("Ingresa otro número\n"))
        print("El resultado de la multiplicación es:",a*b)
        operar = input("¿quiere seguir operando? (s/n)")
        if operar== "n":
            break
    #Division
    elif(y==4):
        a=float(input("Ingresa un número\n"))
        b=float(input("Ingresa otro número\n"))
        if (b==0):
            print("No se puede dividir entre 0") 
        else:
            print("El resultado de la división es:",a/b)
            operar = input("¿quiere seguir operando? (s/n)")
        if operar== "n":
            break
    #Raiz Cuadrada
    elif(y==5):
        print("Ingresa un Numero")
        Raiz= float(input())
        print("Su Raiz Cuadrada es: ",math.sqrt(Raiz))
        operar = input("¿quiere seguir operando? (s/n)")
        if operar== "n":
            break
    #Radianes
    elif(y==6):
        print("Ingrese los Grados")
        Rad= float(input())
        print(Rad,"Grados en radianes son: ",math.radians(Rad))
        operar = input("¿quiere seguir operando? (s/n)")
        if operar== "n":
            break
    #Factorial de un Numero
    elif(y==7):
        print("Ingrese un numero")
        fact= float(input())
        print("El factorial de",fact,"es: ",math.factorial(fact))
        operar = input("¿quiere seguir operando? (s/n)")
        if operar== "n":
            break
    #Hipotenusa de un Triangulo
    elif(y==8):
        print("Ingrese Cateto a")
        Cateto_a= float(input())
        print("Ingrese cateto b")
        Cateto_b= float(input())
        print("La Hipotenusa es:", )
        print(math.hypot(Cateto_a, Cateto_b))
        operar = input("¿quiere seguir operando? (s/n)")
        if operar== "n":
            break
    else:
        print("NUMERO INVALIDO")