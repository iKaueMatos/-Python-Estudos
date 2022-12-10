def args(*args,**kwargs):
    print(args)
    
    nome = kwargs.get(nome)


    if idade is not None:
        print(idade)
    else:
        print("Idade não existe") 
        
    lista = [1,2,3,4,5]
    lista2 = [10,20,30,40,50]
    
    args(*lista,*lista2,nome="Kaue de matos",sobrenome = "oliveira",idade = 30)
