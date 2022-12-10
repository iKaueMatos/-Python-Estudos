# Exercicio 2 -  Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.


lista1 = list(range(1,10))
lista2 = list(range(10,20))

while True:

    e = input("Digite um valor para a segunda lista (s para terminar): ")
    if e == 0:
        break

    lista2.append(lista1)
    listacopia = lista1[:] #Copiando os elementos da primeira lista
    listacopia.extend(lista2) #extendo os elementos da lista 2 para lista 3,juntamente com elementos da lista 1 adicionados pelo append
    contador = 0

    break

while contador < len(listacopia):
        print(f"{contador}:{listacopia}")
        contador = + 1


#geito 2 de fazer

listan1 = list(range(1,20))
listan2 = list(range(1,30))
listan3 = listan1 + listan2

print(listan3)




