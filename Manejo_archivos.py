from io import open

#archivo_texto=open("archivo.txt","w")
# primera ejecución para grabar
#frase="Estupendo día para estudiar Python \n el miércoles"

#archivo_texto.write(frase)

#archivo_texto.close ()

archivo_texto=open("archivo.txt","r")

#lectura sobre un objeto
#texto=archivo_texto.read()

#archivo_texto.close()

#print (texto)

#leer por líneas

lineas_texto=archivo_texto.readlines()

#archivo_texto.close()
#Tratar toda la lista
print (lineas_texto)
#Tratar solo un elemento de la lista
#print (lineas_texto[0])

#archivo_texto=open("archivo.txt","a")

#archivo_texto.write("\n siempre es una buena ocasion para estudiar Python")

#archivo_texto.close()



