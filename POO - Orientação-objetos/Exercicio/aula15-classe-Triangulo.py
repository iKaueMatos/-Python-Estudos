#Crie	um	programa	que	uFlize	esta	classe.	Ele	deve
#pedir	ao	usuário	que	informe	as	medidas	de	um
#triangulo.	Depois,	deve	criar	um	objeto	com	as
#medidas	e	imprimir	sua	área	e	maior	lado.

#Atributos:Lado A, Lado B,Lado C
#Metodos; Calcular Perimetro,getMaiorLado

class Triangulo:
    def __init__(self,ladoA,ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB


    def calculo_lado(self,ladoA,ladoB):
        if ladoA > 0:
            self.ladoA = ladoA
        if ladoB > 0:
            self.ladoB = ladoB

    def retornalados(self):
        return (self.ladoA,self.ladoB)

    def lado_maior(self):
        if lado1 >= lado2:
            print('lado 1 e maior',lado1)
        if lado2 >= lado1:
            print('lado 2 e maior',lado2)

    def calculo_area(self):
        return self.ladoA * self.ladoB

    def calcular_Perimetro(self):
        return (self.ladoA * 2) + (self.ladoB*2)


lado1 = int(input('informe o lado A: '))
lado2 = int(input('informe o lado B: '))
t1 = Triangulo(lado1,lado2)
area = t1.calculo_area()
p1 = Triangulo(lado1,lado2)
perimetro = p1.calcular_Perimetro()
l1 = Triangulo(lado1,lado2)

print('area:',t1.calculo_area())
print('Perfimetro',p1.calcular_Perimetro())
print('Lado maior',l1.lado_maior())

