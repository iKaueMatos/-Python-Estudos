#Objetos Mutaveis Listas,dicionarios
#Objetos Imutavel = strings,numeros ,true ,false ,none

def lista_de_clientes(clientes_interavel,lista = []):
    lista.extend(clientes_interavel)
    return lista

lista_de_clientes1 = ['Fabricio']
clientes1 = lista_de_clientes(['kaue','matos','oliveira'])
clientes2 = lista_de_clientes(['Clea','de','matos','oliveira'])
clientes3 = lista_de_clientes(['Jose'])


print(clientes1)
print(clientes2)