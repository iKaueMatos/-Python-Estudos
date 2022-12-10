
# exercicio : 
notas1 =  [0,0,0,0,0,0,0]
soma_numeros = 0
contador = 0

while contador < 7:
    notas1[contador]=  float(input(f"Digite uma nota{contador}:"))
    soma_numeros += notas1[contador]
    contador += 1
contador = 0
while contador < 7:
    print(f"nota{contador}: {notas1[contador]: }")
    contador += 1
print(f"Media:{soma_numeros / contador: }")