#2.Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.


valor = int(input("Digite seu primeiro numero: "))
contador = 0

while contador < 2:
    
    valor2 = int(input("Digite seu segundo numero: ")) 
    if valor == 0 and valor2 == 0: 
        print("Valor negativo")
        break

    elif valor > valor2: 
        print("Seu numero maior e",valor)
        break
    
    else: 
         if valor2 > valor:
             print("Seu numero maior e",valor2)
             break 