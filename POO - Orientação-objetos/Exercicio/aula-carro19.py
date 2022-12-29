class Carro:
    def __init__(self,nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor


    @motor.setter
    def motor(self,valor):
        self._motor= valor

    @property
    def fabricante(self):
        return self._fabricante


    @fabricante.setter
    def fabricante(self,valor):
        self._fabricante = valor


class Motor:
    def __init__(self,nome):
        self.nome = nome


class Fabricante: 
    def __init__(self,nome):
        self.nome = nome
        
fusca = Carro ('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkswagen 
print(fusca.nome,fusca.fabricante.nome,fusca.motor.nome)
