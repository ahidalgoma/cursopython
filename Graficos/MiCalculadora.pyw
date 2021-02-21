from tkinter import *

root=Tk()

miFrame=Frame(root, width=1200, height=600)

miFrame.pack()

operacion=""
operacion_ant=""
resultado=0

#---------------- pantalla ---------------------------------------
numeroformula=StringVar()
numeropantalla=StringVar()
numeropantalla.set("0")
numeroformula.set("")

formula=Entry(miFrame, textvariable=numeroformula)
formula.grid(row=0, column=1, sticky="w", padx=10, pady=10, columnspan=4)

pantalla=Entry(miFrame, textvariable=numeropantalla)
pantalla.grid(row=1, column=1, sticky="w", padx=10, pady=10, columnspan=4)
pantalla.config(backgroun="black", fg="#03f943", justify="right")

#-------------- pulsaciones teclado ------------------------------
def numeroPulsado(num):
    global operacion
    global operacion_ant
    if operacion!="":
        numeropantalla.set(num)
        operacion_ant=operacion
        operacion=""
    elif not(numeropantalla.get()=="0" and int(num)==0):
        if numeropantalla.get()=="0":
            numeropantalla.set("")
        numeropantalla.set(numeropantalla.get() + num)

#-------------- pulsaciones operadores ---------------------------
def operacionPulsada (ope, numP):

    numeroformula.set(numeroformula.get() + numeropantalla.get() + ope)
 
    if ope=="+":
        suma(numP)
    elif ope=="*":
        multiplica(numP)
    elif ope=="/":
        divide(numP)
    elif ope=="-":
        resta(numP)
    
    

#--------------------- operación suma ----------------------------
def suma(num1):
    global operacion
    global resultado
    resultado+=int(num1)
    operacion="suma"
    numeropantalla.set(resultado)
#--------------------- operación multiplica ----------------------------
def multiplica(num2):
    global operacion
    global resultado
    if resultado!=0:
        resultado*=int(num2)
    else:
         resultado=int(num2)
    operacion="Multiplica"
    numeropantalla.set(resultado)

#--------------------- operación divide ----------------------------
def divide(num3):
    global operacion
    global resultado
    if resultado!=0:
        resultado/=int(num3)
    else:
         resultado=int(num3)
    operacion="Divide"
    numeropantalla.set(resultado)
#--------------------- operación resta ----------------------------
def resta(num4):
    global operacion
    global resultado
    if resultado!=0:
        resultado-=int(num4)
    else:
         resultado=int(num4)
    operacion="Resta"
    numeropantalla.set(resultado)

#-------------------- funcion el_resultado -----------------------
def el_resultado():
    global operacion
    global resultado
    global operacion_ant
    if operacion_ant=="suma":
        numeroformula.set(numeroformula.get() + numeropantalla.get() + " = ")
        numeropantalla.set(resultado+int(numeropantalla.get()))
    elif operacion_ant=="Multiplica":
        numeroformula.set(numeroformula.get() + numeropantalla.get() + " = ")
        if resultado!=0:
            numeropantalla.set(resultado*int(numeropantalla.get())) 
        else:
            numeropantalla.set(int(numeropantalla.get()))
    elif operacion_ant=="Divide":
        numeroformula.set(numeroformula.get() + numeropantalla.get() + " = ")
        if resultado!=0:
            numeropantalla.set(resultado/int(numeropantalla.get())) 
        else:
            numeropantalla.set(int(numeropantalla.get()))
    elif operacion_ant=="Resta":
        numeroformula.set(numeroformula.get() + numeropantalla.get() + " = ")
        if resultado!=0:
            numeropantalla.set(resultado-int(numeropantalla.get())) 
        else:
            numeropantalla.set(int(numeropantalla.get()))


    operacion_ant=""
    operacion="R"
    resultado=0
            
    


# -------------- Fila 1 -----------------------------------------
boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)

boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)

boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)

botonDiv=Button(miFrame, text="/", width=3, command=lambda:operacionPulsada("/", numeropantalla.get()))
botonDiv.grid(row=2, column=4)

# -------------- Fila 2 -----------------------------------------
boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)

boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)

boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)

botonMult=Button(miFrame, text="X", width=3, command=lambda:operacionPulsada("*", numeropantalla.get()))
botonMult.grid(row=3, column=4)

# -------------- Fila 3 -----------------------------------------
boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)

boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)

boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)

botonRest=Button(miFrame, text="-", width=3, command=lambda:operacionPulsada("-", numeropantalla.get()))
botonRest.grid(row=4, column=4)


# -------------- Fila 4 -----------------------------------------
boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)

botoncoma=Button(miFrame, text=",", width=3, command=lambda:numeroPulsado(","))
botoncoma.grid(row=5, column=2)

botonmas=Button(miFrame, text="+", width=3, command=lambda:operacionPulsada("+", numeropantalla.get()))
botonmas.grid(row=5, column=3)

botonIgual=Button(miFrame, text="=", width=3, command=lambda:el_resultado())
botonIgual.grid(row=5, column=4)


root.mainloop()