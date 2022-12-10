num1 = input("digite seu numero: ")
num2 = input("digite seu numero: ")


#Funçoes para converter strings em numeros => isdigit,isdecimal,isnumeric

if num1.isdigit() and num2.isdigit():

    num1 = int(num1)
    num2 = int(num2)

    print(num2+num1)

else:
    print("Não pode converter os numeros para conta")