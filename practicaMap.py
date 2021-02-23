class Empleado():
    def __init__ (self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        return "{} trabaja como {} y tiene un salario de {} €".format(self.nombre, self.cargo, self.salario)

listaEmpleados=[
Empleado("Juan", "Director", 6700),    
Empleado("Ana", "Presidenta", 7500),
Empleado("Antonio", "Administrativo", 2100),
Empleado("Sara", "Secretaria", 2150),
Empleado("Mario", "Botones", 1800)
]

def calculo_comision(empleado):
#de esta forma solo calcula la comisión a los que corresponde pero devuelve toda la lista    
    if (empleado.salario<=3000):
        empleado.salario=empleado.salario * 1.03
    return empleado
# si el return pertenece al if solo devolverá estos empleados para la lista de MAP


listaempleadoscomision=map(calculo_comision, listaEmpleados)

for emple in listaempleadoscomision:
    print(emple)
