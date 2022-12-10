#exercicio 3.4 - escreva uma expresao para determinar
#se uma pessoa deve ou nao pagar imposto considere que pagam imposto cujo salario  seja maior que R$1200

nome = input("Digite seu nome: ")
salario = float(input("Digite seu salario: "))
salarioimposto = int(1200)
imposto = salario / 2

if salario > 1200 and imposto:
    print(f"{nome} pagar imposto de {imposto} ")
else:
    print("Não e necessario pagar imposto!")