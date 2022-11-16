from models.user import User
from dao.usuario import usuario

class UserController():
    def __init__(self) -> None:
            self.users = [
                User(nome="teste", senha="teste", email="teste@email.com"),
                User(nome="banana", senha="banana", email="banana@email.com"),
                User(nome="gato", senha="gato", email="gato@email.com"),
            ]
    
        
    def logarUsuario(self, email, senha):
        print("estou aqui")
        usuario1 = User(nome = None, email = email, senha = senha) 
        for user in usuario.getInstance().logarUsuario(email, senha):
            if user.email == usuario1.email and user.senha == usuario1.senha:
                return True 
        return False
    
    def cadastrarUsuario(usuario):
        return usuario.getInstance().cadastrarUsuario(usuario)
        