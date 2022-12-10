#List comprehension em python 

l1 = list(range (1,10))

#O que estamos falando aqui: Queremos que cada valor seja interado dentro de uma varivel e depois faça alguma coisa com os valores... 
ex1 = [variavel for variavel in l1] 

print("Exemplo 1",ex1)

print()
#Exempo 2

#Basicamente aqui multiplicamos os elementos da lista com o laço For 
ex2 = [v * 2 for v in l1]

print("Exemplo 2",ex2)

print()
#Exemplo 3 
        #O 1 for intera sobre a primeira lista
ex3 = [(v,v2) for v in l1 for v2 in range(3)]

print("Exemplo 3",ex3)

print()
l2 = ["Kauê","Matos","Oliveira"]
#Função replace('a','@') - O que conseguimos fazer com a função replace?,Basicamente para cada letra a da nossa lista
#Alteramos a letra por um @....

#"For v in l2" vamos interar sobre a lista e alterar dos as letras com os valores correspondentes....
ex4 = [v.replace('a','@')for v in l2]

print("Exemplo 4",ex4)


#Exemplo 5: 
print()

tupla = (
    ('chave','valor'),
    ('chave2','valor2'),
)

ex5 = [(y,x) for x,y in tupla]
ex = dict(ex5)

print("Exemplo 5",ex5)

#Exemplo 6:
print()
l3 = list(range(100))
ex6 = [v for v in l3 if v % 2 == 0] 
print("Exemplo 6 numeros pares",ex6) 

#Exemplo 7: 

#Para conseguirmos utilizar o else dentro do nosso for (lista),precisamos inserir primeiramente as condições que serao proposta
#e logo depois inserimos o else para especificar o "SENÃO",é interamos sobre a lista para fazer a verificação completa
print()
ex7 = [v if v % 3 == 0 else "Não e divisivel" for v in l3]

print("Exemplo 7",ex7)