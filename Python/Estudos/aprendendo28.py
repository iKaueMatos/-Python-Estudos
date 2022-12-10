#Para criar um dicionario,podemos criar dessa maneira:
dicionario = dict(
    nome ="kaue de matos oliveira",
    idade =18,
    estado ="são paulo"
)

print(dicionario["nome"])

#Podemos criar dessa maneira tambem: 

dic = {
    "nome":"kaue",
    "idade":19,
    "estado":"São paulo"
}

print(dic["nome"])

#Lembrando que se especificarmos um chave que não existe no nosso 
# dicionario:O programa ira para de funcionar!

#Para conseguirmos contonar isso precisamos fazer uma condição com if especificando o que queremos fazer,Que pode ser uma 
# verificação ou a criação dessa chave

dic["Naoexiste"] = "Agora existe"

#verificando se chave do dicionario existe!
if "Naoexiste" in dic:
    print(dic["Naoexiste"])