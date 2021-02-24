import re

lista_nombre=["Ana Gómez", "Laura Martín", "Sandra López", 
                "Santiago Martin", "Pablo Hidalgo", "Pepe Hidalgo", "Sandra González"]

# empieza por ...
for elemento in lista_nombre:
    if re.findall('^Sandra', elemento):
        print(elemento)

# termina en ...
for elemento in lista_nombre:
    if re.findall('Martín$', elemento):
        print(elemento)

# contiene alguno de los caracteres seguientes ...
for elemento in lista_nombre:
    if re.findall('[Hg]', elemento):
        print(elemento)
# algunos cracteres y sus variantes
for elemento in lista_nombre:
    if re.findall('Mart[íi]n', elemento):
        print(elemento)
