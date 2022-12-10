#INDICES 0123456789........
#  a,b,c,d,e,f,g,h,i

frase = 'O rato roeu a roupa do rei de roma' #interavel
tamanho_frase = len(frase)
contador = 0
nova_string = ''

usuario = input("Qual letra deseja colocar maiuscula ?:  ")


#interação <-

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == usuario:
        #upper deixa uma letra miniscula em maiuscula
        nova_string += usuario.upper()
    else:
        nova_string += letra
        contador += 1

    print(nova_string)
