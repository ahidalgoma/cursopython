# yield from
def devuelve_ciudades(*ciudad):

    for elemento in ciudad:
##        for subelemento in elemento:
            yield from elemento

ciudades_devueltas = devuelve_ciudades("Madrid", "Bilbao", "Barcelona", "Sevilla", "Granada")

for i in range (1,3):
    print (next(ciudades_devueltas))

