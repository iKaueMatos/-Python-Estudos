usuario = input("Nome do usuario: ")
senha = input("Senha do usuario: ")

usuario_bd = 'kaue'
senha_bd = '12345'

if usuario_bd == usuario and senha_bd == senha:
    print("Login autorizado")
else:
    print("usuario e senha invalido")
