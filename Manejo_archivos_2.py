# manejo de punteros en el fichero de texto
archivo_texto=open("archivo.txt","r")

#print (archivo_texto.read())
#posiciona el puntero en el número de carácter que le indicamos
#archivo_texto.seek(11)

#print (archivo_texto.read(11))

#print (archivo_texto.read())


#archivo_texto.seek(len(archivo_texto.read())/2)

archivo_texto.seek(len(archivo_texto.readline()))
print (archivo_texto.read())



archivo_texto.close()
