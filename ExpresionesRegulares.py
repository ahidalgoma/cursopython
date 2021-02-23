import re

cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

textoBuscar="Python"
'''if re.search(textoBuscar, cadena) is not None:
    print (cadena)
else:
    print ("No encontrado")'''

textoEncontrado=re.search(textoBuscar, cadena)

print (textoEncontrado.start())
print (textoEncontrado.end())
print (textoEncontrado.span())

texto2Encontrado=re.findall(textoBuscar, cadena)
print (texto2Encontrado)
print ("Se ha encontrado ", len(texto2Encontrado)," veces")