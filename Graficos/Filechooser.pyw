from tkinter import *
from tkinter import filedialog

root=Tk()

def abrefichero():
    fichero=filedialog.askopenfilename(title="Abrir", filetypes = (("Ficheros de excel","*.xlsx"),
    ("Ficheros de Texto", "*.txt"),("Todos","*.*")))
    print (fichero)

Button(root, text="Abrir Fichero", command=abrefichero).pack()

root.mainloop()