class Carro:
    #Metodo e uma função que esta dnetor da nossa classe
    def __init__(self,nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} esta acelerando')

fusca = Carro('Fusca')
print(fusca.nome)

celta = Carro(nome='Celta')
print(celta.nome)

