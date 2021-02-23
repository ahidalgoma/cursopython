def numero_par(num):
    if num % 2==0:
        return True

numeros=[17, 23, 25, 26, 28, 36, 89]

for ind in numeros:
    if numero_par(ind):
        print (ind)

print (list(filter(numero_par, numeros)))


print (list(filter(lambda numeropar:numeropar % 2==0, numeros)))
