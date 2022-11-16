from typing_extensions import Self

class Product():
    def __init__(self, id, nome, preco, descricao = "") -> None:
        self.id = id
        self._nome = nome
        self._preco = preco
        self.descricao = descricao
    def __str__(self) -> str:
        return f'Produto: ID: {self.id} - Nome: {self.name} - Preço: {self.preco} - Descrição: {self.descricao}'
    
    def getNome(self):
        return self._nome
    
    def getPreco(self):
        return self._preco

    def getDescricao(self):
        return self._descricao