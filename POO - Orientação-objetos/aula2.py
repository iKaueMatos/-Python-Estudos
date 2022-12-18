class Criar:
#Quando uma função ta dentro de uma classe e chamado de metodo
    def __init__(self,nome,sobrenome): #Init = inicializador de atributos!!!
        #para criar atributos com self chamamos dessa maneira no python
        self.nome = nome
        self.sobrenome = sobrenome

criar = Criar('kaue','Matos')
print(criar)