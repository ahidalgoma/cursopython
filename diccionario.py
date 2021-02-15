midiccionario={"Alemania":"Berlin", "Francia":"Paris", "Reino Unido":"Londres", "España":"Madrid"}
print (midiccionario["Francia"])
print (midiccionario)
midiccionario["Italia"]="Lisboa"
print (midiccionario)
midiccionario["Italia"]="Roma"
print (midiccionario["Italia"])
del midiccionario["Francia"]
print (midiccionario)

# tuplas con diccionarios
mitupla=("Andalucía", "Cataluña", "Asturias")
midiccionario2={mitupla[0]:"Sevilla", mitupla[1]:"Barcelona", mitupla[2]:"Oviedo"}
print (midiccionario2)
print (midiccionario2.keys())
print (midiccionario2.values())
print (len(midiccionario))