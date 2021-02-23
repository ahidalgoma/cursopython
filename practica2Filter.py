class Empleado():
    def __init__ (self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        return "{} trabaja como {} y tiene un salario de {} €".format(self.nombre, self.cargo, self.salario)

listaEmpleados=[
Empleado("Juan", "Director", 75000),    
Empleado("Ana", "Presidenta", 85000),
Empleado("Antonio", "Administrativo", 25000),
Empleado("Sara", "Secretaria", 27000),
Empleado("Mario", "Botones", 21000)
]

salarios_altos=filter(lambda emple1:emple1.salario>50000,listaEmpleados)

for empleadosalario in salarios_altos:
    print (empleadosalario)