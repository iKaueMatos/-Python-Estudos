#__dict__ e vars- para atributos de instãncia


class Pessoa:
    ano_atual = 2022 #atributo
    def __init__(self,nome,idade): #instancia
        self.nome = nome
        self.idade = idade


#Basicamente com essa função logo abaixo:Ela ira permitir que retorne o ano que uma pessoa nasceu
    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

p1 = Pessoa('João',35)
#p1.nome = 'EITA'

p1.__dict__['Python'] = 'coisa'#Adicionado um novo valor ao dcionario
p1.__dict__['nome']= 'Fui alterado' #Alterando o valor da chave 'nome'
print(p1.__dict__) # Dicionario com todos os atributos que foram colocados na classe com essa (variavel)

print(vars(p1))