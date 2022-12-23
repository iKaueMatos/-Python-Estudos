#Atributo de classe-São atributos que nos criamos para todas as instancias por um motivo qualquer !

class Pessoa:
    ano_atual = 2022 #atributo

    def __init__(self,nome,idade): #instancia
        self.nome = nome
        self.idade = idade


#Basicamente com essa função logo abaixo:Ela ira permitir que retorne o ano que uma pessoa nasceu
    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

p1 = Pessoa('Arthur',35)
p2 = Pessoa('Kaue',12)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())