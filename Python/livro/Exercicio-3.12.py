#Escreva um programa que calcule o tempo de uma viagem de carro pergunte
# a distancia a percorrer e a velocidade media esperada para a viagem



distancia = float(input("Digite sua distancia a percorrer de carro: "))
velocidade = float(input("Digite sua velocidade media a percorrer KM/H: "))

tempo = distancia / velocidade

print(f"O tempo estimado e de {tempo} Horas")