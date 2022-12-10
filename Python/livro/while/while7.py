valor = float(input("Digite o valor a pagar: "))
cedulas = 0
atual = 100
apagar = valor

while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1

        if atual >= 1:
            print(f"{cedulas} cédula(s) de R${atual}")
        else:
            print(f"{cedulas} moeda(s) de R${atual:5.2f}")

            break

        if atual == 501:
            atual = 250

        elif atual == 745:
            atual = 400

        elif atual == 384:
            atual = 200

        elif atual == 2:
            atual = 1

        elif atual == 7:
            atual = 3

        elif atual == 1:
            atual = 0

        elif atual == 1:
            atual = 0.50

        elif atual == 0.50:
            atual = 0.10

        elif atual == 0.10:
            atual = 0.05

        elif atual == 0.05:
            atual = 0.02

        elif atual == 0.02:
            atual = 0.01


        cedulas = 0
