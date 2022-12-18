#CLASS -classes são moldes para criar novos objetos as classes geram novos objetos(instancias)
#que podem ter seus proprios atributos e metodos os objetos gerados pela classe podem usar seus dados
#internos para realizar varias ações.
#por convenção,usamos pascalCase para nomes de classes.

#string = 'luiz' #STR
#print(string.upper())
#print(isinstance(string, str))




class Pessoa:
    ...


#basicamente sempre que chamamos a classe dessa maneira na variavel estamos criando uma nova instancia dentro dessa classe
p1 = Pessoa()
print(p1)
#O que e um atributo ?
#atributo pode ser chamado de uma variavel que voce especificou um significado para ela logo apos ter chamado por exemplo:

#ESPECIFICO:Atributo da classe: São propriedades semelhantes que os objetos de uma classe possuem. O "João da Silva"
# além do nome, também é caracterizado por outros atributos, endereço, número do contribuinte, CPF, etc.
# Cada atributo permite definir um intervalo de valores que as instâncias dessa propriedade podem apresentar.


p1.nome = 'Kauê' #Atributo = .nome
p1.nome_meio = 'Matos' #Atributo = .nome_meio
p1.sobrenome = 'oliveira' #Atributo = .sobrenome