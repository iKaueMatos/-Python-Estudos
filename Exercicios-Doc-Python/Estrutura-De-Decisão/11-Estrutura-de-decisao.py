#11 - As Organizações Tabajara resolveram 
# dar um aumento de salário aos seus colaboradores
# e lhe contrataram para desenvolver o programa
# que calculará os reajustes

#Faça um programa que recebe o salário de um colaborador e o reajuste seguindo o seguinte critério, baseado
# no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.


print("--------Olá seja bem vindo-----------")


salario = int(input("Digite seu salario atual: "))
salario1 = salario

print(f"Seu salario atual e R${salario1}")
print()

print(" ----- Calculando seu novo salario -----")
print()

if salario <= 280:
    salario = (salario * 20) / 100 
    salario1 = salario + salario1
    print(f"Seu salario antigo era de R$ 280.00,O aumento do seu salario e de R${salario} sua porcetagem de aumento foi de 20%")
    
if salario == 280 or salario <= 700:
    salario =(salario *15) /100
    salario1 = salario + salario1
    print(f"Seu salario antigo  era entre 280 a 700 reais,O aumento do seu salario e de R${salario} sua porcetagem de aumento foi de 15%")
    
if salario == 1500 or salario == 700:
    salario = (salario *10) / 100
    salario1 = salario + salario1
    print(f"Seu salario antigo era entre 700 a 1500 reais,O aumento do seu salario e de R${salario} sua porcetagem de aumento foi de 10%")
    
if salario >= 1500:
    salario = (salario * 5)/100
    salario1 = salario + salario1
    print(f"Seu salario antigo era igual a 1500 reais ou superior ao mesmo,O aumento do seu salario e de R${salario} sua porcetagem de aumento foi de 5%") 
    
print()
print(f"Seu novo salario e R${salario1}")