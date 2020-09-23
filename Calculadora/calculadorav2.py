import tkinter
from tkinter import *
from tkinter import messagebox

#Creación de la ventana de la calculadora
root = tkinter.Tk()
root.geometry("450x500+300+300")
root.resizable(0,0)
root.title("Calculadora SE")

valor = ""
A = 0
operador = ""

#Creación de funciones para asignar valor a cada botón numérico

def btn1click():
    global valor
    valor = valor + "1"
    data.set(valor)

def btn2click():
    global valor
    valor = valor + "2"
    data.set(valor)

def btn3click():
    global valor
    valor = valor + "3"
    data.set(valor)

def btn4click():
    global valor
    valor = valor + "4"
    data.set(valor)

def btn5click():
    global valor
    valor = valor + "5"
    data.set(valor)

def btn6click():
    global valor
    valor = valor + "6"
    data.set(valor)

def btn7click():
    global valor
    valor = valor + "7"
    data.set(valor)

def btn8click():
    global valor
    valor = valor + "8"
    data.set(valor)

def btn9click():
    global valor
    valor = valor + "9"
    data.set(valor)

def btn0click():
    global valor
    valor = valor + "0"
    data.set(valor) 

# Función de botones de operadores
def btn_suma():
    global A
    global operador,valor
    A = int(valor)
    operador = "+"
    valor = valor + "+"
    data.set(valor)

def btn_resta():
    global A
    global operador,valor
    A = int(valor)
    operador = "-"
    valor = valor + "-"
    data.set(valor)

def btn_mult():
    global A
    global operador,valor
    A = int(valor)
    operador = "*"
    valor = valor + "*"
    data.set(valor)

def btn_div():
    global A
    global operador,valor
    A = int(valor)
    operador = "/"
    valor = valor + "/"
    data.set(valor)

#Función de botón de borrar o clear
def btn_clear():
    global A,operador,valor
    valor = ""
    A = 0
    operador = ""
    data.set(valor)


# Función para encontrar el resultado
def resultado():
    global A,operador,valor
    valor2 = valor
    if operador == "+":
        x = int((valor2.split("+")[1]))
        C = A + x
        valor = str(C)
        data.set(valor)
    if operador == "-":
        x = int((valor2.split("-")[1]))
        C = A - x
        valor = str(C)
        data.set(valor)
    if operador == "*":
        x = int((valor2.split("*")[1]))
        C = A * x
        valor = str(C)
        data.set(valor)
    if operador == "/":
        x = int((valor2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error", "Division By 0 Not Supported")
            A = ""
            valor = ""
            data.set(valor)
        else:
            C = int(A / x)
            data.set(C)


# Label  que muestra el resultado
data = StringVar()
lbl = Label(
    root,
    text = "Label",
    anchor = SE,
    font = ("Verdana", 20),
    textvariable = data,
    background = "#ffffff",
    fg = "#000000",
)
lbl.pack(expand = True, fill = "both")

#Sección de creación de frames
btnrow1 = Frame(root)
btnrow1.pack(expand = True, fill = "both")

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both")

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both")

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both")


#Sección de creación de botones
btn1 = Button(
    btnrow1,
    text = "1",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn1click,
)
btn1.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(
    btnrow1,
    text = "2",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn2click,
)
btn2.pack(side = LEFT, expand = True, fill = "both",)

btn3 = Button(
    btnrow1,
    text = "3",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn3click,
)
btn3.pack(side = LEFT, expand = True, fill = "both",)

btnplus = Button(
    btnrow1,
    text = "+",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_suma,
)
btnplus.pack(side = LEFT, expand = True, fill = "both",)

#Botones del Frame2

btn4 = Button(
    btnrow2,
    text = "4",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn4click,
)
btn4.pack(side = LEFT, expand = True, fill = "both",)

btn5 = Button(
    btnrow2,
    text = "5",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn5click,
)
btn5.pack(side = LEFT, expand = True, fill = "both",)

btn6 = Button(
    btnrow2,
    text = "6",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn6click,
)
btn6.pack(side = LEFT, expand = True, fill = "both",)

btnminus = Button(
    btnrow2,
    text = "-",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_resta,
)
btnminus.pack(side = LEFT, expand = True, fill = "both",)

#Botones del Frame3

btn7 = Button(
    btnrow3,
    text = "7",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn7click,
)
btn7.pack(side = LEFT, expand = True, fill = "both",)

btn8 = Button(
    btnrow3,
    text = "8",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn8click,
)
btn8.pack(side = LEFT, expand = True, fill = "both",)

btn9 = Button(
    btnrow3,
    text = "9",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn9click,
)
btn9.pack(side = LEFT, expand = True, fill = "both",)

btnmult = Button(
    btnrow3,
    text = "*",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_mult,
)
btnmult.pack(side = LEFT, expand = True, fill = "both",)

#Botones del Frame4

btnc = Button(
    btnrow4,
    text = "C",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_clear,
)
btnc.pack(side = LEFT, expand = True, fill = "both",)

btn0 = Button(
    btnrow4,
    text = "0",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn0click,
)
btn0.pack(side = LEFT, expand = True, fill = "both",)

btnequal = Button(
    btnrow4,
    text = "=",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = resultado,
)
btnequal.pack(side = LEFT, expand = True, fill = "both",)

btndiv = Button(
    btnrow4,
    text = "/",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_div,
)
btndiv.pack(side = LEFT, expand = True, fill = "both",)

root.mainloop()

