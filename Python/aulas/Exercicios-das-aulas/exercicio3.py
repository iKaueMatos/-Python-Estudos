#execute um programa no qual o usuario entre com a idade do carro caso ovalor sejamenor ou igual a 3 anos imprima "se carro e novo"
#caso contrario "seu carro e velho"

carro = int(input("Digite a quanto tempo você tem o seu carro: "))
modelocarro = input("Qual e modelo do seu carro ?")



if carro <= 3:
    print(f"Seu {modelocarro} carro e novo")
elif carro >= 3:
    print(f"Seu {modelocarro} carro e velho")
