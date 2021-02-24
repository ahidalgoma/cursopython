from Modulos import Funciones_matematicas


class Areas:
    """ Esta clase se usa para el area de figuras geometricas"""
    def area_cuadrado(lado):
        """ Calcula el área de un cuadrado
        elevenado el parámetro recibido al cuadrado"""

        return "el área del cuadrado es " + str(lado*lado)

    def area_triangulo(base, altura):
        """ Calcula el área de un cuadrado
        utilizando los parámetros base y altura, multiplicando ambos y diviendo el resultado por 2"""

        return "el área del triángulo es " + str((base*altura)/2)

#help (Areas)

help (Funciones_matematicas)

#
# print (Areas.area_cuadrado.__doc__)
#print (Areas.area_cuadrado(7))

#help (Areas.area_triangulo)
#print (Areas.area_triangulo(5,7))
