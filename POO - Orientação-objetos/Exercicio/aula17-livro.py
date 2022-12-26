#	Crie uma classe Livro que possui os #atributos nome,	qtdPaginas,	autor	e	preço.
#– Crie os métodos getPreco para obter	o	valor
#do	preco	e	o	método setPreco para setar
#um	novo	valor	do	preco.
#Crie	um	codigo	de	teste

class Livro:
    def __init__(self,qtdpaginas,autor,valor,atual_preco):
        self.qtdpaginas = qtdpaginas
        self.autor = autor
        self.valor = valor
        self.atual_preco = atual_preco

    def getpreco(self):
        return self.valor




precolivro = int(input('Digite o valor do livro: '))
lp = Livro(precolivro)

