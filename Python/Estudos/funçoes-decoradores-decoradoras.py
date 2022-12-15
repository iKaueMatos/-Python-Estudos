def falaoi (valor,cidade):
    return valor + cidade

print(falaoi(valor= 1,cidade=8))


# decorando uma função

def master(funcao): # mastre = mestre em portugues
    def slave(*args,**kwargs): #slave = escravo em portugues
        print('agora estou decorada')
        funcao(*args,kwargs)
    return slave

@master
def fala_oi():
    print('Oi')


def outra_funcao(msg):
    print(msg)


outra_funcao('Olá eu sou kaue')