from tkinter import *
from tkinter import messagebox  # ventanas emergentes
import sqlite3

root=Tk()

# ------------------------- Funciones ----------------------------------
def InfoAdicional():
    messagebox.showinfo("Licencia", "Gestión de Usuarios versión 2.021")

def AvisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def SalirAplicación():
    valor=messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
    if valor=='yes':
        root.destroy()

def crearBasedeDatos():
    miConexion=sqlite3.connect("GestionUsuarios")
    miCursor=miConexion.cursor()
    try:
        miCursor.execute('''CREATE TABLE USUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(50),
            PASSWORD VARCHAR(20),
            APELLIDOS VARCHAR(50),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100))
            ''')
        messagebox.showinfo("Creación de BBDD", "La base de datos ha sido creada con éxito")
    except:
        messagebox.showwarning("¡ATENCION!", "La base de datos ya existe")

def BorrarCampos():
    ID_usuario.set("")
    NOMBRE_usuario.set("")
    PASSWORD_usuario.set("")
    APELLIDOS_usuario.set("")
    DIRECCION_usuario.set("")
    textComentario.delete(1.0, END)
    
def crearUsuario():
    miConexion=sqlite3.connect("GestionUsuarios")
    miCursor=miConexion.cursor()    
#    Datosusuario=NOMBRE_usuario.get(),PASSWORD_usuario.get(),APELLIDOS_usuario.get(),DIRECCION_usuario.get(),textComentario.get("1.0", END)
    try:
        miCursor.execute("INSERT INTO USUARIOS VALUES(NULL, '"+NOMBRE_usuario.get()+
            "','"+PASSWORD_usuario.get()+ 
            "','"+APELLIDOS_usuario.get()+ 
            "','"+DIRECCION_usuario.get()+
            "','"+textComentario.get("1.0", END)+ "')")
#        miCursor.execute("INSERT INTO USUARIOS VALUES(NULL,?,?,?,?,?)",(Datosusuario))
        miConexion.commit()
        messagebox.showinfo("CRUD Usuarios", "Usuario creado con éxito")
    except:
        messagebox.showwarning("CRUD Usuarios", "Usuario NO pudo ser creado")

def LeerUsuario():
    miConexion=sqlite3.connect("GestionUsuarios")
    miCursor=miConexion.cursor()    
    try:
        miCursor.execute("SELECT * FROM USUARIOS WHERE ID="+ID_usuario.get())
        registroUsuario=miCursor.fetchall()
        if registroUsuario==[]:
            messagebox.showwarning("Usuarios","Registro no encontrado")
        for usu in registroUsuario:
            ID_usuario.set(usu[0])
            NOMBRE_usuario.set(usu[1])
            PASSWORD_usuario.set(usu[2])
            APELLIDOS_usuario.set(usu[3])
            DIRECCION_usuario.set(usu[4])
            textComentario.delete(1.0, END)
            textComentario.insert("1.0", usu[5])
        miConexion.commit()
    except:
        messagebox.showwarning("Buscar Usuario", "Usuario NO pudo ser encontrado")

def Actualizarusuario():
    miConexion=sqlite3.connect("GestionUsuarios")
    miCursor=miConexion.cursor()    
    try:
        miCursor.execute("UPDATE USUARIOS SET NOMBRE='" + NOMBRE_usuario.get() +
            "', PASSWORD='" + PASSWORD_usuario.get() + 
            "',APELLIDOS='" + APELLIDOS_usuario.get() + 
            "', DIRECCION='" + DIRECCION_usuario.get() +
            "', COMENTARIOS='" + textComentario.get("1.0", END) +
            "'WHERE ID=" + ID_usuario.get())    
    
        miConexion.commit()
        messagebox.showinfo("CRUD Usuarios", "Usuario actualizado con éxito")
    except:
        messagebox.showwarning("CRUD Usuarios", "Usuario NO pudo ser actualizado")

def BorrarUsuario():
    miConexion=sqlite3.connect("GestionUsuarios")
    miCursor=miConexion.cursor()    
    try:
        miCursor.execute("DELETE FROM USUARIOS WHERE ID="+ID_usuario.get())
        
        miConexion.commit()
        messagebox.showinfo("Base de datos", "Registro borrado con éxito")
    except:
        messagebox.showwarning("Borrar Usuario", "Usuario NO pudo ser borrado")



# -------------------- Terminan las funciones ----------------------------



#----------------------------------------- Menu ---------------------------------------
barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)


BBDDMenu=Menu(barraMenu, tearoff=0)
BBDDMenu.add_command(label="Conectar", command=crearBasedeDatos)
BBDDMenu.add_command(label="Salir", command=SalirAplicación)

BorrarMenu=Menu(barraMenu, tearoff=0)
BorrarMenu.add_command(label="Borrar Valores Pantalla", command=BorrarCampos)

CRUDMenu=Menu(barraMenu, tearoff=0)
CRUDMenu.add_command(label="Crear", command=crearUsuario)
CRUDMenu.add_command(label="Leer", command=LeerUsuario)
CRUDMenu.add_command(label="Actualizar", command=Actualizarusuario)
CRUDMenu.add_command(label="Borrar", command=BorrarUsuario)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia", command=AvisoLicencia)
ayudaMenu.add_command(label="Acerca de", command=InfoAdicional)

barraMenu.add_cascade(label="BBDD", menu=BBDDMenu)
barraMenu.add_cascade(label="BORRAR",menu=BorrarMenu)
barraMenu.add_cascade(label="CRUD", menu=CRUDMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#------------------------------ Pantalla --------------------------------

miFrame=Frame(root, width=1200, height=600)
miFrame.pack()

ID_usuario=StringVar()
NOMBRE_usuario=StringVar()
PASSWORD_usuario=StringVar()
APELLIDOS_usuario=StringVar()
DIRECCION_usuario=StringVar()



LabelID=Label(miFrame, text="ID: ")
LabelID.grid(row=0, column=0, sticky="e", padx=10,pady=10)
cuadroID=Entry(miFrame, textvariable=ID_usuario)
cuadroID.grid(row=0, column=1, padx=10, pady=10)


LabelNombre=Label(miFrame, text="Nombre: ")
LabelNombre.grid(row=1, column=0, sticky="e", padx=10,pady=10)
cuadroNombre=Entry(miFrame, textvariable=NOMBRE_usuario)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

LabelPass=Label(miFrame, text="Password: ")
LabelPass.grid(row=2, column=0, sticky="e", padx=10, pady=10)
cuadroPass=Entry(miFrame, textvariable=PASSWORD_usuario)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show='?')

LabelApellidos=Label(miFrame, text="Apellidos: ")
LabelApellidos.grid(row=3, column=0, sticky="e", padx=10, pady=10)
cuadroApellidos=Entry(miFrame, textvariable=APELLIDOS_usuario)
cuadroApellidos.grid(row=3, column=1, sticky="w", padx=10, pady=10)

LabelDireccion=Label(miFrame, text="Dirección: ")
LabelDireccion.grid(row=4, column=0, sticky="e", padx=10, pady=10)
cuadroDireccion=Entry(miFrame, textvariable=DIRECCION_usuario)
cuadroDireccion.grid(row=4, column=1, sticky="w", padx=10, pady=10)

LabelComentario=Label(miFrame, text="Comentarios ")
LabelComentario.grid(row=5, column=0, sticky="e", padx=10, pady=10)
textComentario=Text(miFrame, width=16, height=5)
textComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert=Scrollbar(miFrame, command=textComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
textComentario.config(yscrollcommand=scrollVert.set)

# ----------------- Frame 2 con los botones ------------------------
miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="Create", command=crearUsuario)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer=Button(miFrame2, text="Read", command=LeerUsuario)
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonModificar=Button(miFrame2, text="Update",command=Actualizarusuario)
botonModificar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrame2, text="Delete", command=BorrarUsuario)
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)



root.mainloop()

miConexion.close()
