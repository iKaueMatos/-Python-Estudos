from datetime import date

nome = "Kauê de Matos Oliveira"
idade = 18
altura = 1.8
peso = 55
dataAtual = 2022
imc = peso / altura **2

#Imc
print(f"{nome} tem {idade} sua altura e de {altura} e seu peso e de {peso}\n "f" E seu imc e de {imc:.2f}")


#Descobrindo a data de nascimento
def dataNascimento(birthDate):
      today = date.today()
      dateA  = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))

      return dateA

print (dataNascimento(date(2003,8,30)),"Yours","years \n" )
print(nome,"a sua idade",idade)