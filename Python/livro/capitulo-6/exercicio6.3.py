#Programa que percorre duas listas 
# e gera uma terceira sem elementos repetidos

lista_primeira = []
lista_segunda = []
terceira = []
usuario = 0
contador = 0

print("Digite 0 para sair do laço de repetição!")

while contador < 7:
    lista1 = int(input(f"Digite um numero para sua primeira lista (Digite 0 para sair da lista): "))
    contador = + 1 
    if lista1 == 0:
        break
    lista_primeira.append(lista1)
    
print(f"Valores que foram adicionados na primeira lista {lista_primeira}")

print("Segunda lista")

while contador < 7:
    lista2 = int(input(f"Digite um numero para sua segunda lista(Digite 0 para sair da lista): "))
    contador = +1 
    if lista2 == 0:
        break   
    lista_segunda.append(lista2)
   
print(f"Elementos da primeira lista e da segunda sendo percorridos: ")
lista_primeira.extend(lista_segunda)

print(lista_primeira)      

print()

lista_primeira = list(set(lista_primeira))

print("Terceira sem elementos repetidos: ",lista_primeira)










    
    


