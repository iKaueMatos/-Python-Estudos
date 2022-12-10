

compras = []
contador = 0

while contador < 5:
    usuario = input("Digite um produto: ")
    
    if usuario == "fim":
        break
           
    compras.append(usuario)
    
for p in compras:
    print(compras)