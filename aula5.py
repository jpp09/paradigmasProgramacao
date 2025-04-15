lista = [-3,100,5,9,-4]

def obtemMaiorNumero(lista: list = []): 
    num = lista[0]
    for i in lista:
        if i > num:
            num = i
    return num




print(obtemMaiorNumero(lista))


