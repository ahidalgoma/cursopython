from tkinter import *
from tkinter import messagebox  # ventanas emergentes

root=Tk()

def InfoAdicional():
    messagebox.showinfo("Procesador de Angel", "Procesador de texto version 2021")

def AvisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def SalirAplicación():
#    valor=messagebox.askquestion("Salir", "Desea salir de la aplicación")
    valor=messagebox.askokcancel("Salir", "Desea salir de la aplicación")
    if valor==True:
        root.destroy()

def CerrarDocumento():
    valor=messagebox.askretrycancel("Reintentar", "No es posible cerrar. El documento esta bloqueado")
    if valor==False:
        root.destroy()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=500, height=400)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=CerrarDocumento)
archivoMenu.add_command(label="Salir", command=SalirAplicación)

edicionMenu=Menu(barraMenu, tearoff=0)
edicionMenu.add_command(label="Copiar")
edicionMenu.add_command(label="Cortar")
edicionMenu.add_command(label="Pegar")


herramientasMenu=Menu(barraMenu, tearoff=0)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia", command=AvisoLicencia)
ayudaMenu.add_command(label="Acerca de", command=InfoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=edicionMenu)
barraMenu.add_cascade(label="Herramientas", menu=herramientasMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

root.mainloop()