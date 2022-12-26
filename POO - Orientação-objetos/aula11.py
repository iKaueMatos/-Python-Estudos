#@staticmthod (METODOS ESTATICOS) são inuteis em Python =)
#Metodos estaticos são metodos que estão dentro da classe,mas não tem
#acesso ao self nem ao cls em resumo,são funções que existem dentro da sua classe

class Classe:
    @staticmethod

#Conceito do static
#Um método estático dentro de uma classe indica que este método pode ser invocado sem a necessidade de que você tenha uma instância desta classe.

#Usos do static
#Em geral, esse modificador é usado pra métodos que criam e retornam instâncias da própria classe, no padrão singleton, mas podem ter outros usos
#como por exemplo operadores de string, muito comuns em bibliotecas terceirizadas.

    def funcao_que_esta_na_classe(*args,**kwargs):
        print('Oi',args,kwargs)

def funcao(*args, **kwargs):
    print('Oi', args,kwargs)


c1 = Classe()
c1.funcao_que_esta_na_classe(1, 2, 3)
funcao(1, 2, 3)
Classe.funcao_que_esta_na_classe(nomeado =1)