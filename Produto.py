class Produto():
    def __init__(self,nome,preco):
        self._nome = nome
        self._preco = preco
        self._qtd = 0

    @property
    def getNome(self):
        return self._nome
    
    @property
    def getPreco(self):
        return self._preco
    
    @property
    def getQtd(self):
        return self._qtd
    
    @property
    def qtdCompra(self):
        qtd = int(input("Você deseja comprar quantas unidades: "))
        self._qtd = qtd
    
    @property
    def total(self):
        return f"| Total: R${round(self._preco * self._qtd,2)}" 

    def __str__(self):
        return f'Produto -> {self._nome} | Preço -> R$:{self._preco}'
    