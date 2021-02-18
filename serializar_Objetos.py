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

coche1=Vehiculos("Mazda", "MX5")
coche2=Vehiculos("Seat", "Leon")
coche3=Vehiculos("Renault", "Megane")

coches=[coche1, coche2, coche3]

fichero=open("Fichero_Coches", "wb")

pickle.dump(coches, fichero)

fichero.close()

del (fichero)

