#Exercicio list compreshion Solução: 

carrinho = []
total = []
carrinho = [carrinho.append(('Produto 1',30,'Produto 2',30,'Produto 3',30))]
total = sum([float(y) for x,y in carrinho])

print(total)
