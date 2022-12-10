#class - e como se fosse uma receita de bolo onde armazena variaveis e funções 
class Conta:
    #init uma função construtora 
    def __init__ (self,numero,titular,saldo,limite):
        print(f"Construindo um objeto {self}")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f"Sacando dinheiro da conta! saldo da sua conta disponivel para sacar: {self.saldo},Nome do titular da conta {self.titular}")

    def deposita(self,valor):
        self.saldo += valor

    def saca(self,valor):
        self.saldo -= valor

