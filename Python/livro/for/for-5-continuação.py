#.....Continuação do Split,join,enumerate em python

#Curiosidade de funções = Função upper - possibilita deixar todas as letras maiusculas
#função - Split - divide ios valores de uma variavel em string para uma lista
#Função - captalize - Converte a primeira letra de uma string em maiuscula

string = 'O brasil e o pais do futebol,O BRASIL DEVE GANHAR'
lista = string.split(' ')
lista_2 = string.split(',')


palavra = ''
contagem = 0

for valor in lista:
    quantidade_vezes = lista.count(valor)

    if quantidade_vezes > contagem:
        contagem = quantidade_vezes
        palavra = valor

    print(f"A palavra que apareceu mais vezes e a {palavra} ({contagem}) x")