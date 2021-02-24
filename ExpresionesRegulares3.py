import re

lista_nombre=["Ana", "Pedro", "María", "Rosa", "Sandra", "Celia"]

print("Elementos que contengan en alguna parte alguna de las siguientes letras O,P,Q,R,S,T")
for elemento in lista_nombre:
    if re.findall('[o-t]', elemento):
        print(elemento)

print("Elementos que inicien con las letras O,P,Q,R,S,T")
for elemento in lista_nombre:
    if re.findall('^[O-T]', elemento):
        print(elemento)

print("Elementos que terminen con las letras o,p,q,r,s,t")
for elemento in lista_nombre:
    if re.findall('[o-t]$', elemento):
        print(elemento)
