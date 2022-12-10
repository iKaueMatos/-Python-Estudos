#ordenação de uma lista

valor = [1,2,4,5,8,7,7,9,63,6,7]


#Len (Retornando o numero armazenado na lista)
for i in range(len(valor)):
    for j in range(len(valor)):
        if valor[i] <= valor [j]:
            temp = valor [i]
            valor [i] = valor[j]
            valor[j] = temp
            valor[j] = temp

print("lista ordenada",valor)