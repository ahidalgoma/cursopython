milista=["María", "Pepe", "Juan", "Luis"]
print (milista[:])
milista.append("Sandra")
print (milista[:])
milista.insert(2, "Angel")
print (milista[:])
milista.extend([5, True, 23.78])
print (milista[:])
print (milista.index("Angel"))
print("Diego" in milista)
milista.remove("Pepe")
print (milista[:])
milista.pop()
print (milista[:])
print (milista[:] * 3)
