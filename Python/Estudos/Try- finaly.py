#Try,except,else e finally

#Finally tem como significado = buscar sempre fechar o aruqivo mesmo que ele tenha sido executado ou ate mesmo tenha apresentado alguma falha
#Por tanto no final do aruqivo ira ter uma rederização de um erro

try:
    print('Abrir o arquivo')

except ZeroDivisionError:
    print('Dividiu zero')


finally:
    print("aquivo fechado")
