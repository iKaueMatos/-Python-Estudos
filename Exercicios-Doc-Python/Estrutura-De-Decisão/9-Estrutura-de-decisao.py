#Faça um Programa que leia três 
# números e mostre-os em ordem decrescente.

 
numero = int(input("Digite seu 1 numero: "))
numero2 = int(input("Digite seu 2 numero: "))
numero3 = int(input("Digite seu 3 numero: "))
    
if numero < numero2:
        numero,numero2 = numero2,numero
if numero < numero3:
        numero,numero3 = numero3,numero
if numero2 < numero3:
        numero2,numero3 = numero3,numero2
        
print(f"A ordem descrecente e{numero},{numero2},{numero3}")