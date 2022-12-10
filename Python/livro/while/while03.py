#Faça um programa para escrever a contagem regressiva do lançamento de um foguete o programa deve imprimir 10,9,8....1,0 e fogo na tela..

import time

x = 10

while x >= 10:
    time.sleep(1)
    x -= 1
    print(f"Fogo na tela {x}")