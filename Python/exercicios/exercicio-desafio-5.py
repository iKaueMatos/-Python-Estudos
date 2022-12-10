#Faça um programa que peça ao usuario para digitar um numero inteiro,informe se este numero e par ou impar.caso o usuario não
#digite um numero inteiro,informe que nao e um inteiro

num1 = int(input("Digite seu primeiro numero: "))
num2 = int(input("Digite seu segundo numero: "))
resultado = 0

if (num1 + num2) / 2 == resultado:
    print(f"Numero par {num1}")
else:
    print(f"Numero impar {num2}")