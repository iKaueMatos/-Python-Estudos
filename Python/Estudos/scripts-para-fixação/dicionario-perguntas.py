print("Texto explicativo: ")

Contador = 0
respostas_certas = 0

perguntas = {
    
    'Perguntas 1 ': { #Dicionario 1 
        #Perguntas dentro do dicionario com chaves e respostas
        "pergunta":"Quanto e 2 + 2 ?", 
        
        "respostas":{
            "a":'1',
            "b":'2',
            "c":'3',
            "d":'4',
        },
        "resposta_certa":'d',
    },
    'Perguntas 2 ': {
        #Perguntas dentro do dicionario com chaves e respostas
        "pergunta":"Quanto e 8 *7 ?",
        
        "respostas":{
            "a":'56',
            "b":'48',
            "c":'50',
            "d":'64',
        },
        
        "resposta_certa":'a',
    },
    'Perguntas 3 ': {
        #Perguntas dentro do dicionario com chaves e respostas
        "pergunta":"Quanto e 8 / 7 ?",
        
        "respostas":{ #respostas = variavel = respostas_rk
            "a":'1,1429',
            "b":'1.000',
            "c":'456',
            "d":'7821',
        },
        "resposta_certa":'a',
    },
}

print()

for pk,pv in perguntas.items():
    print(f"{pk}: {pv ['pergunta']}") #Pergunta acessando o dicionario 
    
    #Regra das aspas caso você de aspas 
    #duplas fora do codigo,consequentemente você vai ter que dar aspas simples fora do codigo - Regra valida para dicionario
    print("Respostas: ")
    for rk,rv in pv['respostas'].items():
        print(f"[{rk}]: {rv}") 
        
    respostas_usuario = input("Digite qual e sua resposta: ")
    print()
    
    
#Condição SE isso for isso e igual a isso SENÃO e igual aquilo:    
    if respostas_usuario == pv["resposta_certa"]:
        print("Você acertou,Meus parabéns")
        respostas_certas +=1
        print()
        
    else:
        while Contador < 3:
            print('Você errou')
            print("Tente novamente: ")
            respostas_usuario = input("Digite novamente a sua resposta: ")
    
    
quantidade_perguntas = len(perguntas)
pgm_acerto = respostas_certas / quantidade_perguntas * 100


print(f"Você acertou equivalente a:",{pgm_acerto})