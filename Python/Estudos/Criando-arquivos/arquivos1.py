#Tabela
#OPERAÇÕES =  'r' - lEITURA  #'w' - escrita,apaga o conteudo se ja existir
#'a' - escrita,mas preserva o conteudo se ja existir
# 'b' - modo binario
#'+' - atualização da leitura e escrita


usuario = input("Informe seu nome completo: ")

if usuario == 'kaue':
    print("Permissão concedida!")

file = open("arquivo1.txt",'w+')
file.write(f'Olá prezado SR.{usuario} tudo bem?  \n')
file.write('Estamos encaminhando esse email para Sr para notifica-lo que sr ganhou na megasena da virada,meus parábens \n')
file.write('por questões de segurança iremos gerar um novo documento para o Sr inserir seus dados pessoais')
file.seek(0, 0)  # Relatividade = Buscando a posição da onde vamos começar a leitura do nosso arquvio
print(file.read())

print("Para gerarmos um nova arquivo por segurança digite seu nome completo abaixo")
nome = input("Digite seu nome: ")

if nome == 'kaue':
    if usuario == 'kaue':
        banco = input("Digite seu banco: ")
        agencia = int(input("Digite sua agencia: "))
        conta = int(input("Digite a sua conta: "))

lista_bancos =['nubank','banco do brasil','itau','santander','caixa']


if banco == lista_bancos:
    print('Verificando banco \n')
    print('Banco valido.....')

print('Gerando um arquivo par aconfirmação de daods: ')

try:
    file = open("dados-pessoais.txt",'w+')
    file.write(f"Banco:{banco}\n")
    file.write(f"Agencia:{agencia}\n")
    file.write(f"Conta:{conta}\n")
    file.seek(0,0)
finally:
    print(file.read())




