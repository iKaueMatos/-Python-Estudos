#https://wiki.python.org.br/EstruturaDeDecisao


#1.Faça um Programa que peça dois números e imprima o maior deles.

contador = 0
numero = int(input("Digite um numero: "))


while contador  < 2:
    numero2 = int(input(f"Digite o seu 2 numero: "))
    if numero > numero2: 
        print("Seu numero maior e",numero)
        break
    else:
        print("Seu maior numero e",numero2)
        break