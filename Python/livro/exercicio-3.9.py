#Escreva um programa que leia a quantidade de dias,horas,minutos e segundos
# do usuario.calcule o total de segundos!

# Um dia vale 24 horas
# 1 hora tem 3600 segundos 60 * 60
#segundos 1 hora vale 60 segundos



dia = int(input("Dias: "))
hora = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))


total_segundos = dia * 24 * 3600 + hora * 3600 + minutos * 60 + segundos

print("Suas informações solicitadas em segundos e igual a",total_segundos)