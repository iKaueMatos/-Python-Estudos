#Função em Python 

def hello(): 
  while True:
      usuario = input("Digite seu nome: ")
      
      if usuario == "Kaue":
        print(usuario)
        break
    
      else:
          print("Nome incorreto tente novamente")


def divisao(n1,n2):
    return n1 / n2  


divide = divisao(50,20)
print("Resultado da divisão: ",divide)

    
  