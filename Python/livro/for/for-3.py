texto = 'Python'
nova_string = ''

#Continue - Pula para o proximo laço de repetição ou condição
#Break - Para a nossa condição ou laço de repetição

for letra in texto:
    if letra == 't':
        nova_string=nova_string+ letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)