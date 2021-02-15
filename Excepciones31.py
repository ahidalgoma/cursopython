import math

def calcula_raiz(num):
    if num<0:
        raise ValueError ("El número introducido no puede ser negativo")
    else:
        return math.sqrt(num)

opc=int(input("introduzca un número para calcular su raiz cuadrada "))

print (calcula_raiz(opc))

print ("Fin del programa")