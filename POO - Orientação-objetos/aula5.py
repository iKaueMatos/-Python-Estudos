import time


grava = input('Digite se a camera via gravar: ')
camera = input('A camera ira filmar?: ')


class Camera:
    def __init__(self,nome,filmando=False):
        #Self -> dados dentro de um objeto
        self.nome = nome
        self.filmando = filmando

    #Metodos -> Metodos dentro de um objeto,juntamente com objetos
    def filmar(self): #Estado 1 - filmar
        if grava in 'rec':
            print(f'{self.nome} esta filmando....')
            self.filmando = True
        elif grava not in 'No':
            print(f'{self.nome} não esta filmando....')

    def stop(self):
        if camera in 'no':
            print(f'{self.filmando} Não esta filmando')
            self.filmando = False
    def fotografar(self): #Estado 2 - fotografar
        if camera in 'yes':
            print(f'{self.filmando} a camera esta filmando e ela não pode tirar fotos! ')
            self.filmando = False




c1 = Camera('Canon')
c2 = Camera('Sony')
c1.filmar()
c1.fotografar()
c1.stop()

c2.fotografar()
c2.filmar()
c2.stop()