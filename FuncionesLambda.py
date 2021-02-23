'''def area_triangulo(base, altura):
    return (base*altura)/2

triangulo1=area_triangulo(5,7)

triangulo2=area_triangulo(9,6)

print (triangulo1)

print (triangulo2)'''

area_triangulo=lambda base, altura:(base*altura)/2

print (area_triangulo(5,7))

print (area_triangulo(9,6))

#alcubo=lambda numero:numero**3
alcubo=lambda numero:pow(numero,3)
print (alcubo(4))

destacar_importe=lambda importe:"¡{}! €".format(importe)

print (destacar_importe(10000))