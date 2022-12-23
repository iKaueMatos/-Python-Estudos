import json


CAMINHO_ARQUIVO = 'aula8-B.json'

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

#Instancias da classe

p1 = Pessoa('Joao',36)
p2 = Pessoa('Helena',21)
p3 = Pessoa('Joana',11)

bd = [vars(p1),p2.__dict__,vars(p3)]
def fazer_dump():
    with open (CAMINHO_ARQUIVO,'w') as arquivo:
        json.dump(bd,arquivo,ensure_ascii=False,indent=2)




#A variável name
#No Python, arquivos .py são chamados de módulos. Cada módulo pode ser executado
# diretamente, como um programa em si, ou importado por outro módulo.
#Precisamos, de alguma maneira, identificar essa diferença. Para isso, temos uma variável nativa que pode nos
# auxiliar nisso - a __name__, que nos indica o nome do contexto em que o módulo está rodando.
#Resumindo, a variável __name__ representa o nome do módulo. Entretanto, quando o módulo é executado por si só como um programa,
# __name__ é definido para ’__main__’, diferente de quando o módulo é importado, no qual o valor fica de fato igual ao nome do módulo.

if __name__ == '__main__': #Basicamente o constructor __name__ serve para verificar se um modulo ou seja um
    # aruqivo que esta snedo importado e igual ao outro caso seja igual estando dentro do if e fazendo essa seguinte validação if __name__ == '__main__'
    # verificando se um modulo e igual ao outro ele não ira  ser executado  (Desta,maneira não mostrara as informações)
    print('ele e o __main__')
    fazer_dump()