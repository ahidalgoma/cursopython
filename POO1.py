class Coche:
#estado inicial de los objetos de esta clase
    def __init__(self):
        self.__LargoChasis=250
        self.__AnchoChasis=120
        self.__Ruedas=4
        self.__Enmarcha=False
    
    def arrancar(self, arrancamos):
        self.__Enmarcha=arrancamos
        
        if (self.__Enmarcha):
            chequeo=self.__chequeo_interno()
        
        if (self.__Enmarcha and chequeo):
            return "El coche está en marcha"
        elif (self.__Enmarcha and chequeo==False):
            self.__Enmarcha=False
            return "Hay problemas en el chequeo. No se puede arrancar"
        else:
            return "El coche está parado"
   
    def estado(self):
        print ("El coche tiene ", self.__Ruedas, " ruedas y un ancho de ", self.__AnchoChasis, 
        " y un largo de ", self.__LargoChasis)
        if (self.__Enmarcha):
            print ("Está en marcha")
        else:
            print ("Está parado")

    def __chequeo_interno(self):
        print ("Realizando chequeo interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False


 
Micoche=Coche()


print (Micoche.arrancar(True))

Micoche.estado()

print ("------------- A continuación creamos el segundo objeto -------------")

Micoche2=Coche()

print (Micoche2.arrancar(False))

Micoche2.estado()




