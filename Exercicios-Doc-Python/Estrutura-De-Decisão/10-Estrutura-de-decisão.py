#10.Faça um Programa que pergunte em que turno você 
# estuda. Peça para digitar M-matutino ou V-Vespertino ou
# N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" 
# ou "Valor Inválido!", conforme o caso.


print("M - Matutino ---- V - Vespertino ----- N - Noturno")
user = input("Digite em qual horario você estuda: ")

if user == "M" or user == "m": 
    print("Bom dia!!")
if user == "V" or user == "v": 
    print("Boa tarde!")
if user == "N" or user == "n":
    print("Boa noite!")