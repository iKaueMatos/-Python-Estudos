#Lambda - função anonima como se fosse a função return

lista = [
    
    ["p1",13],
    ["p2",14],
    ["p3",15],
    ["p4",16],
    ["p5",17],
    
]

lista.sort(key = lambda item:[1],reverse = True)

print(lista)


print()

print("Outra lista")
#outra opção

print(sorted(lista,key=lambda i: [1],reverse=True))