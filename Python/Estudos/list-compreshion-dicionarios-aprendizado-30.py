#Dicionario comprehension python 

lista = [
    
    ('chave','valor'),
    ('chave2','valor2'),
    
]

d1 = { x: y for x,y in lista}
d1 = dict( lista) #Podemos tambem converter utilizano dict('E a variavel')
print('Exemplo 1',d1)


d2 = {x: y for x,y in enumerate(range(5))}

print("Exemplo 2",d2)