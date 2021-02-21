import sqlite3

miConexion=sqlite3.connect("BaseDatosCurso")

miCursor=miConexion.cursor()

# miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',15,'DEPORTES')")

#variosProductos=[
#
#    ("Camiseta", 10, "Deportes"),
#    ("Jarrón", 90, "Cerámica"),
#    ("Camión", 30, "Juguetes")
#]

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", variosProductos)
miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=miCursor.fetchall()
for i in range(len(variosProductos)):
    print (variosProductos[i])
for producto in variosProductos:
    print ("Nombre Producto: ", producto[0], "Precio: ", producto[1], "Sección: ", producto[2])


miConexion.commit()



miConexion.close()