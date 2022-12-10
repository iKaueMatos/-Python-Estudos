#Armazenamento de dados de cadastro; 

Data_storage_list = []

#operação ternario em Python 
def inicio(dados):

    print("---------------Seja bem vindo----------------")

    print("Digite a letra C para se cadastrar",
"Digite a letra L para logar no sistema")


    user = input("Digite qual e a opção de entrada: ") 


#Cadastramento: 

def cadastro(user_novo):
    print("-----------------------------------------------")
    print("Digite suas informações abaixo: ")
    
    user_cadastramento = input("Digite seu nome completo: ")
    age = input("Digite sua idade: ")
    country = input("Digite seu Pais: ")
    state = input("Digite seu estado: ")
    date_birth = input("Digite sua data de nascimento: ")
    email = input("Digite seu Email para cadastro: ")
    senha = input ("crie sua senha: ")
    senha_nvm = input("Digite sua senha novamente")
    
    
    if senha == senha_nvm:
        print("Concluido")
        Data_storage_list.append(user_cadastramento,email,senha)
    else: 
        print("Senha incorreta")
    contador = 0     
    while contador < 1:
        senha_nvm = input("Digite sua senha novamente")
    contador = + 1 
    
    #retornando dados: 
    return(user_cadastramento,email,senha)





#If checando se o usuario ja e cadastrado,juntamente com função de cadastro

def loggin ():
    print("Insira sua informações abaixo: ")
    print()
    nome_loggin = input("Digite seu nome de usuario: ")
    loggin_senha = input("Digite sua senha de acesso: ")   

#if validando no banco de dados....

if user == L or l:
    print("Usuario ja cadastrado,efetuar o loggin......")
    loggin()
    
else:
    print("Usuario não esta cadastrado,efetuar cadastro!")
    cadastro()

  