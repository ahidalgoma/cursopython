class Persona():

    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=lugar_residencia
    
    def descripcion(self):
        print ("Nombre ", self.nombre, "\nEdad ", self.edad, "\nResidencia ", self.lugar_residencia)


class Empleado(Persona):
    def __init__(self, Salario, Antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.Salario=Salario
        self.Antiguedad=Antiguedad

    def descripcion(self):
        super().descripcion()
        print ("Salario ", self.Salario, "\nAntiguedad ", self.Antiguedad, " años")

Antonio=Empleado(1200,10, "Antonio", 55, "España")

Antonio.descripcion()

print ("Antonio es una persona", isinstance(Antonio, Persona))

Manuel=Persona("Manuel", 45, "Colombia")

Manuel.descripcion()

print ("Manuel es un empleado", isinstance(Manuel, Empleado))
