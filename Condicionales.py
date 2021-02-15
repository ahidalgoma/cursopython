def evaluacion(nota):
    if nota<5:
        valoracion="insuficiente"
    elif nota<6:
        valoracion="suficiente"
    elif nota<7:
        valoracion="bien"
    elif nota<9:
        valoracion="notable"
    else : 
        valoracion="sobresaliente"
    return(valoracion)

print ("Evaluación de notas de alumnos")

nota_introducida=int(input("Introduzca la nota del alumno "))


print ("La valoracion del alumno es "+evaluacion(nota_introducida))