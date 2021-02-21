from tkinter import *

root=Tk()

miFrame=Frame(root, width=1200, height=600)

miFrame.pack()

minombre=StringVar()
LabelNombre=Label(miFrame, text="Nombre: ")
LabelNombre.grid(row=0, column=0, sticky="e", padx=10,pady=10)
cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, sticky="w", padx=10, pady=10)
cuadroNombre.config(fg="green", justify="center")

LabelApellidos=Label(miFrame, text="Apellidos: ")
LabelApellidos.grid(row=1, column=0, sticky="e", padx=10, pady=10)
cuadroApellidos=Entry(miFrame)
cuadroApellidos.grid(row=1, column=1, sticky="w", padx=10, pady=10)

LabelDireccion=Label(miFrame, text="Dirección: ")
LabelDireccion.grid(row=2, column=0, sticky="e", padx=10, pady=10)
cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=2, column=1, sticky="w", padx=10, pady=10)

LabelUsuario=Label(miFrame, text="Usuario: ")
LabelUsuario.grid(row=3, column=0, sticky="e", padx=10, pady=10)
cuadroUsuario=Entry(miFrame)
cuadroUsuario.grid(row=3, column=1, sticky="w", padx=10, pady=10)

LabelPass=Label(miFrame, text="Password: ")
LabelPass.grid(row=4, column=0, sticky="e", padx=10, pady=10)
cuadroPass=Entry(miFrame)
cuadroPass.grid(row=4, column=1, sticky="w", padx=10, pady=10)
cuadroPass.config(show='*')

LabelComentario=Label(miFrame, text="Comentarios ")
LabelComentario.grid(row=5, column=0, sticky="e", padx=10, pady=10)
textComentario=Text(miFrame, width=16, height=5)
textComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert=Scrollbar(miFrame, command=textComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
textComentario.config(yscrollcommand=scrollVert.set)

def CodigoBoton():
    minombre.set("Angel")

boton=Button(root, text="Enviar", command=CodigoBoton)

boton.pack()


root.mainloop()