def lupo():
    cano_longo = int(input("Digite a referencia do produto: "))
    tamanho_meia = input("Digite o tamanho do produto: ")

    if cano_longo == 3245 or 3860:
        file = open("Estoque_meia.txt",'a+')
        if tamanho_meia == 'G' or 'M' or 'm' or 'g':
            file.write(f"{tamanho_meia}")
            selecionado_add = input("Digite em qual tamanho você que adicionar a quantidade: ")
            if selecionado_add == 'G' or 'M':
                quantidade = int(input(f"Informe a quantidade para inserir no tamanhado {selecionado_add}")
        file = open('Estoque_meia.txt','w+')
        file.write(f"{selecionado_add} = {quantidade}")


