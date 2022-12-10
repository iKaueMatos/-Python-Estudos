nome = input("Digite seu nome ")
idade = input("Digite sua idade ")

idade = int(idade)

#limite para pegar emprestimo

idade_maior = 18
idade_menor = 15

if idade >= idade_maior and idade_menor <= idade:
    print(f"{nome} Pode pegar o emprestimo")
else:
    print(f"{nome} Você nao pode pegar o emprestimo")