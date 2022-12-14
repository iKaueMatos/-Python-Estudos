import math

PI = math.pi

def dobra_lista(lista):
    return [x*2 for x in lista] #dobrando valores de uma lista


lista = [1,2,3,45,678,97744,45]
print(dobra_lista(lista))


def multi(lista):
    r = 1
    for i in lista:
        r *= 1
    return r