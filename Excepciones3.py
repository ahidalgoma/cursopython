def evalua_edad(edad):
    if edad<0:
        raise TypeError("No se permiten edades negativas")
    elif edad<20:
        return "eres muy joven"
    elif edad<40:
        return "eres joven"
    elif edad<65:
        return "eres maduro"
    
    return "Perteneces a la tercera edad"

while True:

    try:
        Edad_persona=int(input("Introduce tu edad "))
        print (evalua_edad(Edad_persona))
        break
    except ValueError:
        print ("Introduzca un valor válido")

