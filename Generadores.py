def generapares(limite):
    
    num=1

    listapares=[]
    
    while num<limite:
        listapares.append(num*2)
        num = num + 1
    
    return listapares

def generayipares(limite):

    num=1

    while num<limite:
        yield num*2
        num = num + 1

listapares = generayipares(10)

print (generapares(10))

#for i in listapares:
#   print (i)

# uso del next
print (next(listapares))
print ("aqui más código")

print (next(listapares))
print ("aqui más código")

print (next(listapares))
print ("aqui más código")

