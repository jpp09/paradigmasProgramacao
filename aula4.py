from Produto import Produto

menu = {
    "bebidas": [Produto("Coca-cola",8),Produto("Chá",5),Produto("Energetico",12),Produto("Sprite",8)],
    "Prato principal" : [Produto("Feijoada",20),Produto("Filés com Fritas",25),Produto("Bife a cavala",35)],
    "Sobremesa" : [Produto("Petit Gateau",35),Produto("Açaí",25),Produto("Sorvete",25)]
}

def bebidas():
    count = 1
    print(f'{"-"*10}{"bebidas".upper()}{"-"*10}')
    for bebida in menu["bebidas"]:
        print(f'{count}° - {bebida}')
        count+= 1
    choice = int(input("Digite qual o n° do item desejado: "))
    menu["bebidas"][choice - 1].qtdCompra
    return choice - 1

def pratoPrincipal():
    count = 1


escolhas = []
choice = -1
while(choice != 0):
    
    print("""
Digite a opção desejada:
1 - Escolher Bebidas
2 - Escolher Prato Principal
3 - Escolher Sobremesas
""")
    choice = int(input("Qual opção desejada: "))
    if choice == 1:
        escolhas.append(menu["bebidas"][bebidas()])
    elif choice == 2:
        escolhas.append(menu["Prato principal"][pratoPrincipal()])

total = 0
for produto in escolhas:
    print(f"{produto} {produto.total}")
        

    
    

    
