

class carrinho():
    def __init__(self, idCarrinho, idUsuario, idProduto = "") -> None:
        self.idCarrinho = idCarrinho
        self._idUsuario = idUsuario
        self._idProduto = idProduto
        
    def __str__(self) -> str:
        return f'Carrinho: ID: {self.idCarrinho} - IdUsuario: {self.idUsuario} - IdProduto: {self.idProduto}'
    
    def getIdCarrinho(self):
        return self._idCarrinho
    
    def getIdUsuario(self):
        return self._idUsuario

    def getIdProduto(self):
        return self._idProduto