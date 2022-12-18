class Animal:

    def __init__(self,nome):
        self.nome = nome

        variavel = 'Hello world'
        print(variavel)

    def comendo(self,alimento):
        return f'{self.nome} esta comendo um {alimento}'


    def executar (self,*args,**kwargs):
       return self.comendo(*args,**kwargs)



leao = Animal(nome='Leão')
print(leao.nome)
print(leao.executar('Cachorro'))
