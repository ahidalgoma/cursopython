import math

def calcula_raiz(num):
    if num<0:
        raise ValueError ("El número introducido no puede ser negativo")
    else:
        return math.sqrt(num)

opc=int(input("Introduzca un número para calcular su raiz cuadrada "))

try:
    print (calcula_raiz(opc))
except ValueError as ErrorNumeroNegativo:
    print (ErrorNumeroNegativo)

print ("Fin del programa")