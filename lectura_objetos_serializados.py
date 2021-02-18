import pickle

class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True
    
    def estado(self):
        print ("Marca ", self.marca, "\nModelo ", self.modelo)
        if (self.enmarcha):
            print ("Está en marcha")
        else:
            print ("Está parado")
        if (self.acelera):
            print ("Está acelerando")
        else:
            print ("No está acelerando")
        if (self.frena):
            print ("Está frenando")
        else:
            print ("No está frenando")


ficheroApertura=open("Fichero_Coches", "rb")

miscoches=pickle.load(ficheroApertura)

ficheroApertura.close()

for c in miscoches:
    print (c.estado())

