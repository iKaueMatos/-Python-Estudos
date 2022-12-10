usaurio_data_science = [15,23,43,56]
usuarios_machine_learning = [13,23,56,42]


assisistiram = usaurio_data_science.copy()
assisistiram.extend(usuarios_machine_learning)


#Len utilizado para obter um numero de itens em uma lista
if len(assisistiram) == 8:
    #Função set pega os conjuntos de numeros reais e inteiros,E não permite repetir em uma lista...
    #desta maneira excluindo os numero repetidos...
    print(set(assisistiram),"Dicionario")
else:
    print(len(assisistiram)) 
    
    
#podmeos pedir para set também devolver uma lista de conjuntos numericos selecionando o mesmo
#**LEMBRANDO** Que a função SET ira ignorar elementos repetidos... 

