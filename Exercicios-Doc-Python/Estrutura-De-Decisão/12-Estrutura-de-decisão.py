#12 - Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto 
# de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a
# 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto 
# menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.

 #       Salário Bruto: (5 * 220)        : R$ 1100,00
  #      (-) IR (5%)                     : R$   55,00  
   #     (-) INSS ( 10%)                 : R$  110,00
    #    FGTS (11%)                      : R$  121,00
     #   Total de descontos              : R$  165,00
      #  Salário Liquido                 : R$  935,00


usuario_hora = float(input("Digite o valor da sua hora: "))      
trabalhadas_mes = float(input("Digite as horas trabalhadas no mês: "))

salario_bruto = usuario_hora * trabalhadas_mes

print()

if salario_bruto <= 900:
    desconto = 0.0
if salario_bruto <= 1500:
    desconto = 5 
elif salario_bruto <= 2500:
    desconto = 10 
else:
    desconto = 20
    
#Folha de pagamento; 

IR = salario_bruto * (desconto / 100)
INSS = salario_bruto * (desconto / 100)
FGTS = salario_bruto * (desconto /100 )

desconto_tl = IR + INSS

salario_liquido = salario_bruto - desconto_tl

print(
    
    f"\nSalário Bruto     : R${salario_bruto}",
    f"\n(-) IR (5%)       : R${IR}",
    f"\n(-) INSS ( 10%)   : R${INSS}",
    f"\nFGTS (11%)        : R${FGTS}",
    f"\nTotal de descontos: R${desconto_tl}",
    f"\nSalário Liquido   : R${salario_liquido}",
    
    
    
    
    
)