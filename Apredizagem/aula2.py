valores = [10,11,1,1,2,2,2,5,5,5,7,7,7,4]
pares = []
impar = []
contador = 0

for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impar.append(valor)
        
print(f"Valores pares de uma lista {pares},valores impar de uma lista {impar}")