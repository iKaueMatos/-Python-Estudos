l1 = [1,2,3]
l2 = [4,5,6,7]
l4 = [4,5,6,7,8,9]
#estamos concatenando a lista 1 e lista 2
l3 = l1 + l2
print(l3)


#Basicamente ela extende uma lista da continuação nela,pegando o valor a l2 e
# completando na lista principal
l1.extend(l2)

print(l1)

#Exemplo 2 Extend, você pode incluir mais um valor na sua lista por meio da função Extend

l4.extend('Aprendendo')

#Função append - insere um novo valor no final da nossa lista


l5 = [1]
l5.append('10')
#Basicamente estamo acesentando mais um indice para nossa,lista
print(l5)


#insert  possibilita que escolhemos o lacal = indice onde vamos inserir o nossa string ou numero

l6 =[5,7,8,9,10]

#ele ira inserir um valor no determinado indice escolhido pelo desenvolvedor e logo depois ira reajustar toda a lista(trocando todos os indices)
l6.insert(0,'banana')

print(l6)

#Pop remove o ultimo elemento da sua lista!
