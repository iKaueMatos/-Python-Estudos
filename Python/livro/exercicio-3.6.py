#escreva uma expressão que sera utilizada para decidir se um aluno foi ou nao aprovado para ser
# aprovado todas as medias do aluno devem ser maiores que 7.considere que o aluno cursa aprenas três materias e quea nota de cada uma
#esta armazenada nas seguintes variaveis materia 1,materia 2,materia 3

nc = input("Digite sua nota de Noções de direito")
fisica = input("Digite sua nota de Fisica para computação")
ihc = input("Digite sua nota de Interação humana computador")

media = (nc + fisica + ihc) / 3

if media >= 7:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")