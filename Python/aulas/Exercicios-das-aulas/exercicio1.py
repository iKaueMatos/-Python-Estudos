#escreva um programa no qual leia dois valores numericos e imprima o maior deles caso
# ambos os numeros forem iguais,imprima na tela "numeros iguais"

nome = input("Digite seu nome: ")
nome_usuario = "kaue"
senha = input("Digite sua senha: ")
senha_usuario = 12

#Função
def numeromaior():

    number = int(input("Digite um numero "))
    number1 = int(input("Digite o seu segundo numero "))

    if (number > number1) and number == number1:
        print(f"O maior numero {number}")
    elif (number1 > number):
        print(f"O seu numero maior e {number1}")




    # nome do usuario
    if nome_usuario == nome and senha_usuario == senha:
        print(f"nome do usuario {nome_usuario} correto {senha_usuario} correta")
        numeromaior()
    else:
        print("Nome icorreto")
        numeromaior()
        #fim
