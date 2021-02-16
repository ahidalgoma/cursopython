class Coche ():
    def desplazamiento(self):
        print ("Me desplazo utilizando cuatro ruedas")

class Moto():
    def desplazamiento(self):
        print ("Me desplazo utilizando dos ruedas")

class Camion():
    def desplazamiento(self):
        print ("Me desplazo utilizando seis ruedas")

def desplazamientoVehiculo(Vehiculo):
    Vehiculo.desplazamiento()

Micoche=Coche()
Mimoto=Moto()
Micamion=Camion()

print ("------- coche -------")
desplazamientoVehiculo(Micoche)
print ("------- moto -------")
desplazamientoVehiculo(Mimoto)
print ("------- Camión -------")
desplazamientoVehiculo(Micamion)

