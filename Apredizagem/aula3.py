lugares_vagos = list(range(1,10))
usuario = int(input("Digite o lugar que você quer ser adicionado: "))
quantidade_lugares = []


while True: 
    sala = int(input("Digite 0 para sair,Ou digite a sala que você quer entrar: "))
    if sala == 0:
        print("Fim") 
    break

if sala > len(lugares_vagos) or sala < len(lugares_vagos):
    print("Adicionando....")
    
            
else: 
    print("Sala cheia,ou invalida")
    
    
    

        
    
