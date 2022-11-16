import sqlite3
from src.models.product import product

class carrinhoController:
    _instance = None
    
    def __init__(self) -> None:
        self._connect()
        
    @classmethod
    def getInstance(cls):
        if cls._instance == None:
            cls._instance = carrinho()
        return cls._instance
    
    def _connect(self):
            self.conn = sqlite3.connect('./Databases/SQLite.db')
            
    def addCarrinho(self, usuario, produto):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            INSERT INTO carrinho(fkUsuario, fkproduto) VALUES
            (
                '{carrinho.asd}',
                '{pedido.id_cliente}',
                {pedido.quantidade},
                '{pedido.numero_pedido}',
                '{pedido.data_hora}'
            );
        """)
        self.conn.commit()
        self.cursor.close()