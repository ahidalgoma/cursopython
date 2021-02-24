def funcion_decoradora(funcion_parametro):

    def funcion_interior():
        # Acciones adicionales que decoran
        print ("Vamos a realizar el cálculo", funcion_parametro)

        funcion_parametro()

        print ("Hemos terminado el cálculo", funcion_parametro)
    
    return funcion_interior

@funcion_decoradora
def suma():
    print (15+20)

@funcion_decoradora
def resta():
    print (20-15)

suma()

resta()