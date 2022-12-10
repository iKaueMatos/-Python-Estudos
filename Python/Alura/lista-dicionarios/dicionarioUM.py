
#Função - teste = conta
def cria_conta (numero,titular,saldo,limite,valor):
    #Dicionario:
    conta2 = {
       "numero":numero,
        'titular':titular,
        'saldo':saldo,
        'limite':limite
    }
    return conta2

def deposita (conta,valor):
    conta["saldo"] += valor

def saque(conta,valor):
    conta["saldo"] -= valor


def extrato(conta):
    print(f"saldo e {conta['saldo']}")




