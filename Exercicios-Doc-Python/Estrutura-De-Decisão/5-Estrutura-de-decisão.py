#5.Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota = int(input("Digite a sua primeira nota: "))
contador = 0

while contador < 1: 
    nota1 = int(input("Digite a sua 2 nota: "))    
    media = (nota + nota1) / 2
    
    if media == 10: 
        print("Aluno aprovado")
    else:
        print("Aluno reprovado") 
        
    
