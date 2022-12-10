contador = 1
acumulador = 1

while contador <= 10:
    print("Bem vindo a seu Laço de repetição")
    print(contador,acumulador)

    if contador > 5:
        break
    acumulador = acumulador + contador
    contador += 1
else:
    print('cheguei no else')

