#Faça um programa que pergunte a hora ao usuario e,baseando-se no
# horario descrito,exiba a saudação apropriada

nome = input("Digite seu nome: ")
pgthora = float(input("Digite a sua hora atual: "))
dia = "ja esta manhã"
tarde = "ja esta tarde"
noite = "ja esta noite "

if pgthora == 8 or pgthora == 12:
    print(f"Bom dia,{nome} já são {dia}")
elif pgthora == 13 or pgthora == 17:
    print(f"boa tarde,{nome} já são {tarde}")
elif pgthora == 18 or pgthora == 23:
    print(f"Boa noite,{nome} já são {noite}")