import pickle

class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print ("Ha creado una persona de nombre ", self.nombre, " con ", self.edad, "años", 
        "y de genero ", self.genero)
    
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.edad, self.genero)

class ListaPersonas:
    personas=[]
    
    def __init__(self):
        ListadePersonas=open("FicheroExterno", "ab+")
        ListadePersonas.seek(0)
        try:
            self.personas=pickle.load(ListadePersonas)
            print ("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print ("El fichero esta vacio")
        finally:
            ListadePersonas.close()
            del (ListadePersonas)

    def Agregarpersona (self, p):
        self.personas.append(p)
        self.GuardarPersonasenFicheroExterno()
    
    def Mostrarpersonas (self):
        for p in self.personas:
            print (p)

    def GuardarPersonasenFicheroExterno(self):
        ListadePersonas=open("FicheroExterno", "wb")
        pickle.dump(self.personas, ListadePersonas)
        ListadePersonas.close()
        del(ListadePersonas)

    def MostrarinfoFicheroExterno(self):
        print ("La información contenida en el fichero externo es la siguiente:")
        for c in self.personas:
            print (c)



Milista=ListaPersonas()

persona=Persona("Ana", "Femenino", 19)

Milista.Agregarpersona(persona)

Milista.MostrarinfoFicheroExterno()