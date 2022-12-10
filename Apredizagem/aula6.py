 #Programa fila resolução simplificada:
 
fila = list(range(1,11))

print(f"Quantidade de clientes na fila {len(fila)} \n")

usuario_prosseguir = input("Deseja prosseguir ? digite 1 para continuar: ")

while True:
    if usuario_prosseguir == 1:
        print("Inicializando! ") #prosseguindo  
        usuario_add = input("Digite F para adicionar clientes ou A para adicionar,na fila ou 0 para sair: ")    
