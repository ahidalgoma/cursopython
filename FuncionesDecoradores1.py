def funcion_decoradora(funcion_parametro):

    def funcion_interior(*args, **kwargs):
        # Acciones adicionales que decoran
        print ("Vamos a realizar el cálculo", args, kwargs)

        funcion_parametro(*args, **kwargs)
#       La siguiente instruccion falla si usamos kwargs
#        print ("Hemos terminado el cálculo de {} y {}".format(args[0], args[1]))
        print ("Hemos terminado el cálculo")    
    return funcion_interior

@funcion_decoradora
def suma(num1, num2):
    print (num1+num2)

@funcion_decoradora
def resta(num1, num2):
    print (num1-num2)

@funcion_decoradora
def potencia (base, exponente):
    print (pow(base, exponente))

suma(7,5)

resta(12,10)

potencia(base=5,exponente=3)