#Escreva um programapara calcular a redução do tempo de vida de um fumante.pergunte a quantidade de cigarros fumados por dia
#E quantos anos ele ja fumou.consider que um fumante perde 10 min de vida a cada cigarro e calcule quantos dias de vida um
# fumante perdera.exiba o tatal em dias


Usuario = int(input("Quantos Cigarros ja foram fumados por dia ?: "))
anos = int(input("Quantos Anos você ja fumou cigarro?: "))
reduçao = anos * 365 * Usuario * 10

diasreduçao = reduçao / (24*60)

print(f"Redução do tempo de vida{diasreduçao}")

