#	Crie uma classe Livro que possui os #atributos nome,	qtdPaginas,	autor	e	preço.
#– Crie os métodos getPreco para obter	o	valor
#do	preco	e	o	método setPreco para setar
#um	novo	valor	do	preco.
#Crie	um	codigo	de	teste

class Livro:
    def __init__(self,novo,qtdpagina,escolha):
        self.qtdpagina = qtdpagina
        self.novo = novo
        self.escolha = escolha

    def getantigo(self): #return valor do livro atual
        return self.qtdpagina,self.novo,self.escolha

    def setatual(self): #valor a ser calculado
        self.escolha = int(input("Escolha qual foi sua opção para compra Codigo limpo[1], Introdução ao Python[2]: "))
        self.qtdpagina = float(input(f"Digite a quantidadade de pagina do seu livro:{self.escolha} para obter o valor total com o cupom de desconto: "))
        if self.escolha == 1 or self.escolha == '2':
            self.calculo = (self.novo /100) * self.qtdpagina - self.qtdpagina



usuario = input("Digite seu nome: ")
lp = Livro()
atual_livro = lp.getantigo() #retorna valor do livro atual
preco_novo = lp.setatual()
print(f"Olá Sr.{usuario},seu livro tem total de R${atual_livro}")
print(f"Com cupom de desconto aplicado pelo Sr{usuario} o livro ira ficar {preco_novo}")




