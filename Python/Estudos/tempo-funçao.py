from time import time
from time import sleep
def velocidade(funcao):
    def interna(*args,**kwargs):
        start_time = time()
        resultado = funcao(*args,**kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'A função {funcao.__name__} levou {tempo}ms para executar')
        return resultado()
    return interna()
@velocidade
def demora(): #Funçao demora de ser executada
    for i in range(5):
        print(f"volta no laço {i}")
        sleep(1)# segundos

demora()
