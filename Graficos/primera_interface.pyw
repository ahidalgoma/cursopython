from tkinter import *

raiz=Tk()

raiz.title("Ventana de prueba")

# posibilidad de que no se pueda redimensionar una ventana raiz.resizable(0,0)

# raiz.iconbitmap("user.ico")

#raiz.geometry("650x350")

raiz.config(bg="blue")
raiz.config(bd=45)

raiz.config(relief="groove")

raiz.config(cursor="hand2")


miFrame=Frame()

#miFrame.pack(fill="both", expand="True")

miFrame.pack()

miFrame.config(bg="red", width="650", height="350")

miFrame.config(bd=35)

miFrame.config(relief="sunken")

#miFrame.config(cursor="hand2")

miFrame.config(cursor="pirate")

raiz.mainloop()
