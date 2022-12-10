
nome = "Kaue"
idade = 18 # Numeiro inteiro
altura = 1.80 # float
e_maior = idade > 18
data_1 = True #booleano
peso = 50
imc = peso / (altura **2)


print('Nome:', nome)
print('idade: ',idade)
print('Altura:',altura)
print('E maior:',e_maior)

print(nome,"tem",idade,"Anos de idade e seu imc e",imc)

#conseguimos arredodar nossos codigos simplemente definindo a quantidade de casa decimais que queremos que aparece por meio do
# codigo .quatidade de casa decimais que voce quer que apareça f
print(f'{nome} tem {idade} anos de idade e seu imc e {imc:.2f}')

print('{} tem {} anos de idade e seu imc e {}'.format(nome,idade,imc))





