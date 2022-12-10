#Split,JOIN,Enumerate em Python

# * Split - dividir em string
# * Join - juntar uma lista com uma string
# * Enumerate - Enumerar elementos da lista / List interaveis = No caso listas são interaveis e strings também!

#Split,explicação = basicamente ela possibilita que você pegue uma variavel que esta em string e transforme em lista

string = 'O brasil e o pais do futebol,O BRASIL DEVE GANHAR'
#colocando a função split entre aspas basicmante abre a porta para nós fazermos um vriavel em string,ser uma
# lista com espaço entre as palavras completas,e as palavras solitarias tipo O,E,OU
lista = string.split(' ')

print("Lista diferente!")
print()
#Agora conseguimos abrir a porta para a função split colocar , no espaço aplicado na lista!
lista_2 = string.split(',')

print(lista)

#Laço for conseguimos definir o nome que queremos,E chamar nossa variavel e dessa maneira aplicar nossa estrutura de codigo!

for valor in lista:

    #Função count possibilita que = contamos quantas vezes cada palavra aparece na frase
    print(f"A palavra valor apareceu {valor}, {lista.count(valor)} x na frase ")


