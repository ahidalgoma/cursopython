def area_triangulo(base, altura):
    """ Esta función calcula el area de un triangulo. Multiplica la base, que es el primer parámetro, 
    por la altura, que es el segundo parámetro
    
    >>> area_triangulo(3,6)
    'El area del triángulo es: 9.0'
    
    >>> area_triangulo(4,6)
    'El area del triángulo es: 12.0'
    """ 

    return "El area del triángulo es: "+str((base*altura)/2)


import doctest
doctest.testmod()