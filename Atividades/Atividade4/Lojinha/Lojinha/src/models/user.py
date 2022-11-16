class User():
    def __init__(self, nome, email, senha , **kwargs):
        self.nome = nome
        self.email = email
        self.senha = senha  
        
    def __str__(self) -> str:
        return f'User(Nome:{self.nome} - Email: {self.email} - Senha: {self.senha})'