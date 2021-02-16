NombreUsuario=input("Introduzca Nombre de Usuario: ")

print ("El nombre es: ", NombreUsuario)

print ("El nombre es: ", NombreUsuario.upper())

print ("El nombre es: ", NombreUsuario.lower())

Edad=input("Introduce tu edad: ")
while (Edad.isdigit()==False):
    print ("Por favor introduce un valor numérico")
    Edad=input("Introduce tu edad: ")

if (int(Edad)<18):
    print ("No Puede pasar")
else:
    print ("Puede Pasar")


