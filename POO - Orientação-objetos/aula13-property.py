class Caneta:
    def __init__(self, cor):
        self._cor = cor   # _antes de coloca ro nome do atributo = se referindo diretamente para o metodo property
#dizendo assim que convensão e que não deve ser utilizado


    @property
    def cor(self):
        print('caneta normal')
        return self._cor
    @cor .setter
    def cor(self,valor):
        if not valor == 'Rosa':
            raise ValueError('Não aceito esa cor')
        print('Estou no setter',valor)
        self._cor = valor


def mostrar(caneta):
    return caneta.cor


caneta = Caneta('azul')
caneta.cor = 'Rosa'

print(caneta.cor)