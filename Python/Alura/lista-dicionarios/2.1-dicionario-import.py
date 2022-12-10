
#chamando o codigo de função e Importando a função em um codigo
# principal com os seus = parametros funções
from dicionarioUM import cria_conta,deposita,saque,extrato
from dicionario_classe import ContaCorrente


#Atribuindo valores a variavel conta 2 na lista de dicionarios.....
conta2 = cria_conta(123,"kaue",55.0,1000)

#Depositando valores por meio da função crianda no dicionario
deposita(conta2, 15.0)

#Mostrando o extrato do deposito
extrato(conta2)


conta2 = {
    
        "numero": 321,
        "limite":200.0
    
}

deposito(conta2, 500.0)


#Utilizando a classe


#referencia conta para saber onde irar encontrar o objeto = Nossa classe
conta = ContaCorrente(3000)
