import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()

miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confección'")

productos=miCursor.fetchall()

for i in productos:
    print (productos)

miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")

miConexion.commit()

miConexion.close()