
#

velocidade = int(input("Digite sua velocidade atual"))
multa = velocidade - 80 * 5.00


if (velocidade > 80):
    print(f"Você ultrapsso a velocidade e sera multado em {multa}")
else:
    print("Você não foi multado")
