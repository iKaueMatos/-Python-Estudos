from function import lupo

print("Seja bem vindo! ")

usuario = input("Informe seu nome: ")
lista_produtos = ["Lupo [L]","Mash [M]","Trifil [T]","Nayane [N]","Ligerie [Lg]"]


if usuario == "teste" or usuario == 'teste':
    print("Acesso liberado!!!")

print("Escolha o produto que sera adicionado")
produtos = input(f"Digite a letra do produto para acessa-lo {lista_produtos}: ")


if produtos == "L" or produtos == "l":
    produto_add = input("Nome do produto que vai ser adicionado: ")

    if produto_add == 'Meia cano longo' or 'meia':
        print("Criando o arquivo! \n")
        file = open(f"Estoque_{produto_add}.txt",'w+')
        print("Produto adicionado")
        file.write(f"Estoque do {produto_add}")
        file.write(f"Meias Cano longo \n")
        file.write(f"{produto_add}")
        lupo()

else:
    while True:
        produto_add = input("Digite o nome do produto correto")

