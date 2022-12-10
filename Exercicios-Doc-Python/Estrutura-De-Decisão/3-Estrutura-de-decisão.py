#3.Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

print()
print("Masculino ou feminino")
letra_digitada = input("Digite uma letra para verifica se e masculino ou feminino: ")


if letra_digitada == 'M': 
    print("Letra digitada M - Masculino ")
    
elif letra_digitada == 'F':
    print("Letra digitada F - Feminino")
    
else: 
    print("Sexo invalido")


