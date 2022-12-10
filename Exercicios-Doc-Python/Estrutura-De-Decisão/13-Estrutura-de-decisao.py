#13.Faça um Programa que leia um número e exiba o dia correspondente da semana. 
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.



print("------Seja bem vindo descubra agora que dia da semana e hoje----------- ")

usuario = int(input("Digite o dia para a verificação: "))

def dia(): #Function
    if usuario == 1:
        print ('1-Domingo')
    elif usuario == 2:
        print ('2-Segunda')
    elif usuario == 3:
        print ('3-Terça')
    elif usuario == 4:
        print ('4-Quarta')
    elif usuario == 5:
        print('5-Quinta')
    elif usuario == 6:
        print ('6-Sexta')
    elif usuario == 7:
        print ('7-Sabádo') 


#Code
if usuario == 1:
        print ('1-Domingo')
elif usuario == 2:
        print ('2-Segunda')
elif usuario == 3:
        print ('3-Terça')
elif usuario == 4:
        print ('4-Quarta')
elif usuario == 5:
        print('5-Quinta')
elif usuario == 6:
        print ('6-Sexta')
elif usuario == 7:
        print ('7-Sabádo')
else:
    print ('Numero invalido') 
    while True:        
        print("Digite novamente de 1 a 7")
        usuario = int(input("Digite o dia para a verificação: "))
        if usuario == dia():
            dia()
        break
          
           

   



