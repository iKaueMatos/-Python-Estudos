#Lista e multavel
conta_do_kaue = 700
conta_Millena = 800

def deposita_para_duas(contas):
    for conta in contas:
        conta.deposita(100)

contas = [conta_do_kaue,conta_Millena]
print(contas[0],contas[1])

deposita_para_duas(contas)
print(contas[0],contas[1])
