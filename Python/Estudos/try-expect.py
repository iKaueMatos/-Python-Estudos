# TRY - E bem semelhante ao If se a codição tal for verdadeira execute isso se nao excute
# EXCEPT- Que e um comando bem semelhante ao ELSE


#Exemplo 1

try:
    print("kaue de matos oliveira")
except:
    print("Erro")


#Exemplo 2 codigo complexo 


nome = input("Digite seu nome? ")


while nome == 'kaue':
    try:
        print("parabéns você passou")
        break

    except Exception as erro:
        print("Ocorreu um erro inesperado")

    else:
        print(nome)
    