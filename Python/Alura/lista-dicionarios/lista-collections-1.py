idades = [39,37,55,44,60,30]

#Mostra a quantidade de valores interios da lista - função Len()
print(len(idades))
#Adiciona um valor no final da sua lista!
idades.append(15)


#Ira passar dentro da lista e logo depois ira remover o valor 30
for idade in idades:
    print(idade)
#Função remove() - remove um valor da lista!
idades.remove(30)

#Remove todos os elementos da sua lista!
idades.clear()