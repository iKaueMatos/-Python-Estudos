while True:
    print()
    num_1 = int(input("Digite um numero: "))
    num_2 = int(input("Digite outro numero: "))
    operador = input("Digite um operador: ")




# / * - +



    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print("Nenhum operador foi digitado!")
