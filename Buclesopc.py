for letra in "Python":
    if letra=="h":
        continue
    print ("Viendo la letra " + letra)

nombre="Pildoras Informáticas"
print ("Longitud variable total" + str(len(nombre)))
contador=0
for i in nombre:
    if i==" ":
        continue
    contador+=1
print ("Longitud sin blancos" + str(contador))