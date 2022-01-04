class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self._preco = self._preco - (self._preco * (percentual / 100))

    # getter
    @property
    def preco(self):
        print("retornar o preço")
        return self._preco

    # setter
    @preco.setter
    def preco(self, novo_valor):
        print("atualizar preço")
        if isinstance(novo_valor, str):
            raise ValueError("O valor deve ser um número inteiro")
        self._preco = novo_valor
    
    @preco.deleter
    def preco(self):
        print("Deletar preco")
        del self._preco