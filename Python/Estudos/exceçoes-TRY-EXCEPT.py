def divide (n1,n2):
    if n2 == 0:
        raise ValueError("n2 não pode ser 0")
    return n1 /n2


#Basicamente estamos tratando esta função caso o usuario digite um coisa que não queremos que ele digite
try:
    print(divide(n1=2,n2=4))
except ValueError as error:
    print("Você esta tentanto dividir um valor zero")
    #print(error)

