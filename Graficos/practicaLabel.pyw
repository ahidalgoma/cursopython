from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

#miLabel=Label(miFrame, text=" Hola Mundo ")

#miLabel.place(x=100, y=200)

#miImagen=PhotoImage(file="modeloer.gif")

Label(miFrame, text=" Hola Mundo ", fg="red", font=("Comic Sans MS", 36)).place(x=100, y=100)

#Label(miFrame, image=miImagen).place(x=100, y=100)

root.mainloop()




