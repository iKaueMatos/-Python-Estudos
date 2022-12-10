#continuação

usuario = [
    ("Kaue de matos oliveira",30,2003),
    ("Aleatorio",40,2010),
    ("Nunca nem vi",40,2015)
]

#DESEPACONTADO Tudo =


#Laço de repetição
for nome,idade,nascimento in usuario:
    print(nome)

    # Laço de repetição for lista tupla metodo _ siginificado não ira colar os dados da
    # lista meio que sera removido

    for nome, _, _ in usuario:
        print(nome)


