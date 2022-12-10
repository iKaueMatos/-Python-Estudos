#Faça um programa que calcule o aumento de um salario.
# ele deve slicitar o valor do salario e a porcetagem deaumento.exiba o valor do aumento!

salario = float(input("Digite seu salario: "))
aumento = int(input("Digite a porcetagem do aumento: "))
nvsalario = salario * aumento / 100

print(f"O aumento do seu novo salario e de {nvsalario} Seu salario atual agora e de: {nvsalario + salario}")