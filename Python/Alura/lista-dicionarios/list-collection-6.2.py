idades = list(range(1,21))

print("Lista 1 - Reversed")
print("Lista 1,usando tuplas",list(reversed(idades)))

print("Lista 2 - Função")

print(sorted(idades,reverse = True)) #Sempre verdadeiro - Fução que tambem ordena a lista


print("Lista 3 - Função")

nomes = ["kaue",'Matos','oliveira'] #Conseguimos comparar tambem as listas por meio do comando sorted,utilizando as,
# ordem das letras como se fosse um alfabeto
print(sorted(nomes))#Devemos lembrar que as letras maiusculas serão exibidas primeiro e logo em seguida as minisculas



