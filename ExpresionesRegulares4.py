import re

# Buscar en Google patrones busqueda python

Lista_nombres=["Sandra López", "Antonio Gómez", "sandra López"]

for nom1 in Lista_nombres:
    if re.match("Sandra", nom1, re.IGNORECASE):
        print ("match --> Hemos encontrado el nombre Sandra al principio")
    else:
        print("match --> No hemos encontradoel nombre Sandra al principio")

for nom1 in Lista_nombres:
    if re.search("López", nom1):
        print ("search --> Hemos encontrado el nombre López")
    else:
        print("search --> No hemos encontrado el nombre López")

Lista2_nombres=["Jara López", "Antonio Gómez", "Lara López"]
for nom2 in Lista2_nombres:
    if re.match(".ara", nom2, re.IGNORECASE):
        print ("Hemos encontrado el nombre")
    else:
        print("No lo hemos encontrado")

Lista3_nombres=["Sandra López", "23242526", "a2324252"]

for nom1 in Lista3_nombres:
    if re.match("\d", nom1):
        print ("Inicia con un numero")
    else:
        print("No inicia con número")
