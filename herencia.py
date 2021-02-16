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

class Furgoneta(Vehiculos):

    def carga(self, cargar):
        cargado=cargar
        if (cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

class Moto(Vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"
    
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
                
        print (self.hcaballito)

class Velectricos(Vehiculos):
    def __Init__(self, marca, modelo):
        super().__init__(marca_VE, modelo_VE)
        self.autonomia=100
    
    def CargarEnergia(self):
        self.cargando=True

class Bicicletaselectricas(Velectricos,Vehiculos):
    pass

Mimoto=Moto("Honda", "CBR")

Mimoto.caballito()

Mimoto.estado()

print ("------------------ Furgoneta -----------------")
Mifurgoneta=Furgoneta("Mercedes", "CLK")

Mifurgoneta.arrancar()

Mifurgoneta.estado()

print (Mifurgoneta.carga(True))

print ("------------ Bicicletas Electricas -------------")

Mibici=Bicicletaselectricas("Orbea","HC1030")

Mibici.estado()

