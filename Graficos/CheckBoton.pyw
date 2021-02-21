from tkinter import *

root=Tk()
root.title("Elige Destino")

playa=IntVar()
montana=IntVar()
rural=IntVar()

def opcionesviaje():
    opcionescogida=""
    if (playa.get()==1):
        opcionescogida+=" playa"
    if (montana.get()==1):
        opcionescogida+=" Montaña"
    if (rural.get()==1):
        opcionescogida+=" Turismo Rural"

    textofinal.config(text=opcionescogida)


foto=PhotoImage(file="modeloer.png")
Label(root, image=foto).pack()

miFrame=Frame(root)
miFrame.pack()

Label(miFrame, text="Elige destino", width=50).pack()

Checkbutton(miFrame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesviaje).pack()
Checkbutton(miFrame, text="Montaña", variable=montana, onvalue=1, offvalue=0, command=opcionesviaje).pack()
Checkbutton(miFrame, text="Turismo Rural", variable=rural, onvalue=1, offvalue=0, command=opcionesviaje).pack()

textofinal=Label(miFrame)
textofinal.pack()


root.mainloop()