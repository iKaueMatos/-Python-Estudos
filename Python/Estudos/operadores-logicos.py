#operadores logicos

# and,or,not
#in e not in

a = 2
b = 2
c = 3

#AND É - Verifica se as duas comparações são verdadedeiras  e se caso forem verdadeiras
# retornara true que e verdadeiro111111111111111111111111111111111111111111
#Caso uma comparação seja verdadeira e outra falsa retornara = falso

a == b and b < c



#OR OU - Verifica se uma comparaçao e verdadeiro OU Verdadeiro, Basicamente ele verifica se as
# duas comparaçoes sao verdadeiras caso sejam verdadeiras sera retornado um valor
#para retornar as duas comparações tem que ser verdadeiras

a == b or b < c


#NOT  NÃO - Basicamente a porta logica NOT ira inverter as expressões então se antes um valor era
# verdadeiro ele passara a ser falso apos ser verificado

if not b > a:
    print("B E maior que A")
else:
    print('A e maior que B')


# IN - ESTÁ - Basicamente a funçao da porta logica IN e verificar se
# exite algo em uma determinada variavel caso exista isso sera exebido

nome = "kaue"

if "a" in nome:
    print(f"Existe a letra A no seu nome {nome}")
else:
    print("Não existe essa letra dentro do seu nome")

# IN NOT Não estiver - Invertendo a expressão

user = "kaue"

if "k" not in nome:
    print("Existe")
else:
    print("existe o texto")
