#Escreva um programa que exiba a tabuada do numero digitado de 0 a 10

n = int(input("Tabuada do: "))
x = 1

while x <= 10:
    print(f"{n} x {x} = {n * x}")
    x = x + 1
