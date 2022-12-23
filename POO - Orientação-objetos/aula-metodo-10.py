#Metodo normal = Recebe uma instancia e permite que você exiba a mesma,basicamente você tem que passar a classe e identificar como um atributo self!!

#Metodo de classe =

class Pessoa:
    ano = 2023 #atributo classe

    def __init__(self,nome,idade,estado):
        self.nome = nome
        self.idade = idade
        self.estado = estado

    @classmethod #Permite você chamar uma classe sem receber SELF,mais e neessario receber um parametro
    def metodo_de_classe(cls):
        print('Hey')


    @classmethod
    def estado(cls, estado,nome):
        return cls(nome, 50,estado)


p3 = Pessoa.estado('Kaue','São paulo')
print(p3.nome,p3.idade,p3.estado)

