
while True:

    cpf = input("Digite seu cpf: ")
    novo_cpf = cpf[:-2] #Elimina os dois ultimos digitos do CPF
    reverso = 10 #Contador reverso
    total = 0

    for index in range(19):
        if index > 8:  #Primeiro indice vai de 0 a 9, 
            index -= 9 #São os 9 primeiro digitos do CPF
        print(cpf[index], reverso)

        total += int(novo_cpf[index]) * reverso #Valor total da multiplicação
        print("resultado do total", total)

        reverso -= 1 #Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            digito = 11 - (total % 11)
            if digito > 9:
                digito = 0
            total = 0
            novo_cpf += str(digito)

    if cpf == novo_cpf:
        print("valido")
    else:
        print("Cpf invalido")
