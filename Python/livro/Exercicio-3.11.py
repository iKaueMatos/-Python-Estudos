#Faça um programa que solicite o preço de umamercadoria e o percentual de desconto.exiba o valor do desconto e preço a pagar
valorProduto = float(input("Digite o valor do seu produto: "))
desconto = float(input("Desconto: "))
descontoAplicado = valorProduto * desconto / 100
valorTotal = valorProduto - descontoAplicado

print(f"Valor a Pagar: {valorTotal}")



