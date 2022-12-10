#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo o usuario,assim como a quantidade de dias
# pelos quais o carro foi alugado.
# calcule o preço a pagar,sabendo que o carro custa R$ 60 por dia R$0,15 por KM rodado.


Usuario = input("Digite seu Nome: ")
Km = int(input("Digite a quantidade de Km percorrido: "))
Dia = int(input("Digite a quantidade de Dias que você ficou com o carro: "))
Valorkm = 60
valordia = 0.15

print(f"Total a pagar e de:{Km * Valorkm + Dia * valordia}")