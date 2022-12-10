idades = [1,2,4,5,6,7,8]

idade_ano_que_vem = []
#Basicamente vamos sempre pegar um valor e adicionar a uma lista que esta vazia resultando
#Em um conjunto formando uma lista[]
for idades_ano in idades:
    idade_ano_que_vem.append(idades_ano + 1)

    print(idade_ano_que_vem)


print()
#sintaxe menos complexa

#PARA CADA IDADE SOMA + 1
idades_ano_talvez = [(idade + 1) for idade in idades]

print(idades_ano_talvez)

print()

#Filtrando as idades
idades_ano_talvez2= [(idade)for idade in idades if idade > 21]

print(idades_ano_talvez2)