def divide():
    while True:
        try:
            opc1 = int(input("Introduce el primer número "))
            opc2 = int(input("Introduce el segundo número "))

            print ("El resultado de la operación es " + str(int(opc1/opc2)))
            break
        except ValueError:
            print ("Valores inválidos. Introduzca valores válidos ")
        except ZeroDivisionError:
            print ("No se puede dividir por 0")
        finally:
            print ("Cálculo finalizado")    

divide()