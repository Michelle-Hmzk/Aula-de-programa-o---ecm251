from operator import truediv
import sqlite3
from src.models.user import User

class usuario:
    _instance = None

    def __init__(self) -> None:
        self._connect()

    @classmethod
    def getInstance(cls):
        if cls._instance == None:
            cls._instance = usuario()
        return cls._instance
        
    def _connect(self):
            self.conn = sqlite3.connect('./database/SQLite.db')
    
    def getAll(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM usuario;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(User(nome=resultado[0], email=resultado[1], senha=resultado[2]))
        self.cursor.close()
        return resultados
    
    def cadastrarUsuario(self, usuario):
            self.cursor = self.conn.cursor()
            self.cursor.execute("""
                INSERT INTO usuario (nome, email, senha)
                VALUES(`{usuario.nome}`, `{usuario.email}`,`{usuario.senha}`);
            """)
            self.conn.commit()
            self.cursor.close()
        
    def logarUsuario(self, email, senha):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM usuario 
                WHERE email = '{email}' AND senha = '{senha}';
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(User(nome=resultado[0], email=resultado[1], senha=resultado[2]))
        self.cursor.close()
        return resultados
    
    