class Aumentosalario:
    def __init__(self,salario,nome,aumento):
        self.salario = salario
        self.nome = nome
        self.aumento = aumento


    def retorna_valores(self):
        return self.salario,self.aumento
    def calculo_aumento(self):
        return (self.salario / 100) * self.aumento


    def novo_salario(self):
        return self.aumento + self.salario



nome = input('Digite seu nome: ')
salario_atual = int(input('Digite seu salario atual: '))
aumento = int(input('Digite o valor do seu aumento: '))


ca = Aumentosalario(salario_atual,nome,aumento)
s1 = salario_atual

calcular_aumento1 = ca.calculo_aumento()
nv_salario = ca.novo_salario()

print('Meus parabéns',nome,'pela promoção')
print('O salario atual e',s1)
print('Seu aumento e de',ca.calculo_aumento())
print('Seu salario com o aumento e:',ca.calculo_aumento() + ca.novo_salario())
