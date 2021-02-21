from tkinter import *
from tkinter import messagebox  # ventanas emergentes
import sqlite3

root=Tk()

miConexion=""
miCursor=""

def InfoAdicional():
    messagebox.showinfo("Licencia", "Gestión de Usuarios versión 2.021")

def AvisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def BBDDCreada():
    messagebox.showinfo("Creación de BBDD", "La base de datos ha sido creada con éxito")

def BBDDNoCreada():
    messagebox.showinfo("Creación de BBDD", "No se pudo crear la base de datos")

def SalirAplicación():
    valor=messagebox.askquestion("Salir", "Desea salir de la aplicación")
    if valor=='yes':
        root.destroy()

def conectarBasedeDatos():
    global miConexion
    global miCursor
    miConexion=sqlite3.connect("GestionUsuarios")

    miCursor=miConexion.cursor()

def crearBasedeDatos():
    try:
        conectarBasedeDatos()
        miCursor.execute('''CREATE TABLE USUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(50),
            PASSWORD VARCHAR(20),
            APELLIDOS VARCHAR(50),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(500))
            ''')
        BBDDCreada()
    except:
        BBDDNoCreada()

def BorrarCampos():

#----------------------------------------- Menu ---------------------------------------
barraMenu=Menu(root)
root.config(menu=barraMenu, width=500, height=400)


BBDDMenu=Menu(barraMenu, tearoff=0)
BBDDMenu.add_command(label="Conectar", command=crearBasedeDatos)
BBDDMenu.add_command(label="Salir", command=SalirAplicación)

BorrarVCampos=Menu(barraMenu, tearoff=0)
BorrarVCampos.add_command(label="Borrar Valores Pantalla", command=BorrarCampos)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia", command=AvisoLicencia)
ayudaMenu.add_command(label="Acerca de", command=InfoAdicional)

barraMenu.add_cascade(label="BBDD", menu=BBDDMenu)
barraMenu.add_cascade(label="BORRAR",menu=BorrarVCampos)
barraMenu.add_cascade(label="CRUD")
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)



root.mainloop()

miConexion.close()
