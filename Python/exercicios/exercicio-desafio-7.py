#Faça um programa que peça o primeiro nome do usuario.se voce tiver 4 letras ou menos escreve "seu nome e curto";
#se tiver 5 e 6 letras,escreva "seu nome e normal";maior que 6 escreva "seu ome e muito grande".


nome = input("Digite seu nome: ")
tamanho = len(nome)


if tamanho <= 4:
    print("Seu nome e curto")
elif tamanho <= 6:
    print("Seu nome e normal")
else:
    print("Seu nome e grande")
