#Relaçao entre classes associação,agregação e composição
#composição e uma especialização da agregação.
#Mas nela,quando objeto 'pai' for apagado,todas
#as referencias dos objetos filhos tambem são apagadas.

class Cliente:
    def __init__(self,nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self,rua,numero):
        self.enderecos.append(Endereco(rua,numero))

    def inserir_endereco_externo(self,endereco):
        self.enderecos.append(endereco)

    #instancia exibindo os endereços
    def listar_endereco(self):
        for endereco in self.enderecos:
            print(endereco.rua,endereco.numero)


#instancia
class Endereco:
    def __init__(self,rua,numero):
        self.rua = rua
        self.numero = numero


cliente1 = Cliente('Kaue')
cliente1.inserir_endereco('Av.Paulista',54)
cliente1.inserir_endereco('Rua B',6745)
endereco_externo = Endereco('Av.Saudade',123213)
cliente1.inserir_endereco_externo(endereco_externo)
cliente1.listar_endereco()


#Exibindo na tela
print(cliente1.enderecos[0].rua)
print(cliente1.enderecos[1].rua)
cliente1.listar_endereco()