#objetivo saber qual e a posição de cada elemento,Utilizando indce




#Meio do LEN
idades = [15,87,65,56,32,49,37]


#laço de repetição
for i in range(len(idades)):
    print(i,idades[i])


#2 laço de repetição

print("Segunda lista")

lista1 = range(len((1,9)))

enumerate(lista1)

lista2 = list(range(len(lista1)))

lista3= list(enumerate(lista2))


print(lista3)

#Laço 3 enumerate junto com for

#lista tupla
print("Terceiro valor")
for indice in enumerate (lista1):
    contador =+ 1
    print(indice, "x", lista1)







