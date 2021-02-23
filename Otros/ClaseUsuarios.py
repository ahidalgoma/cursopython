from tkinter import *

root=Tk()

class usuario():
    def __init__(self):
        self.id_usu="0"
        self.nombre_usu="por defecto"
        self.password_usu=""
        self.apellidos_usu=""
        self.dirección_usu=""
        self.comentarios_usu=""

    def crear_usu(self, registro):
        self.id_usu=registro[0]
        self.nombre_usu=registro[1]
        self.password_usu=registro[2]
        self.apellidos_usu=registro[3]
        self.dirección_usu=registro[4]
        self.comentarios_usu=registro[5]
        print (miusu.id_usu, miusu.nombre_usu, miusu.password_usu, miusu.apellidos_usu, miusu.dirección_usu, miusu.comentarios_usu)

    def empaquetar_usu(self):
#        registro2=(self.id_usu, self.nombre_usu, self.password_usu, self.apellidos_usu, self.dirección_usu, self.comentarios_usu)
        return (self.id_usu, self.nombre_usu, self.password_usu, self.apellidos_usu, self.dirección_usu, self.comentarios_usu)


miusu=usuario()
registro_usu=["1", "Angel", "passAngel", "Hidalgo", "Lecrin", "Comentarios de Lecrin"]

miusu2=usuario()
miusu2.id_usu="2"
miusu2.nombre_usu="Pepe"
miusu2.password_usu="PassPepe"
miusu2.apellidos_usu="Marin"
miusu2.dirección_usu="Huetor Vega"
miusu2.comentarios_usu="Comentarios de Pepe"

boton=Button(root, text="Prueba", width=3, command=lambda:miusu.crear_usu(registro_usu))
boton.pack()

print (miusu2.empaquetar_usu())



root.mainloop()