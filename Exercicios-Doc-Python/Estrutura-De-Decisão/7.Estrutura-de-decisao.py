#7.Faça um Programa que leia três números e mostre o maior e o menor deles.

primeiro = int(input('Primeiro numero: '))
segundo  = int(input('Segundo numero : '))
terceiro = int(input('Terceiro numero: '))

maior = primeiro
menor = primeiro

if (segundo > maior):
        maior = segundo
if (terceiro > maior):
        maior = terceiro
print('Maior: ',maior)

#Menor nuemro 
print("Mostre o menor numero")

primeiro = int(input('Primeiro numero: '))
segundo  = int(input('Segundo numero : '))
terceiro = int(input('Terceiro numero: '))

menor = primeiro

if (segundo < menor):
        menor = segundo
if (terceiro < menor):
        menor = terceiro
print('Menor: ',menor)





