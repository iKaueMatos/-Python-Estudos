#Modulos padrão do python:
#Modulos são arquivos . py (que contem codigo python) e servem para expandir as funcionalidades padão da linguagem
# As funcionalidades padrão da linguagem.
# Veja todos os modulos padrão em:
#docs.python




#Immportando um Criando-um-modulo
from sys import platform as so #Verificando em qual plataforma o seu dispositivo esta executando este codigo
from sys import platform


print(platform)
print("simplificado",so)


#Modulo random

import random

for i in range(10):
    print(random.randint(0,10))



