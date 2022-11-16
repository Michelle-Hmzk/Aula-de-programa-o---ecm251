from turtle import onclick
import streamlit as st
import pages.Home as home
from models.user import User
import controller.userController as UserController

st.set_page_config(
    page_title="PokeMart",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded",
)

login, cad = st.tabs(["Login", "Cadastro"])

with login:
    st.title("Login")

    col1, col2= st.columns([3,1])
    with col1:
        email = st.text_input(
            "Email:",
            key="iptEmailLogin",
            placeholder = "email@email.com"
        )
        senha = st.text_input(
            "Senha: :",
            key="iptSenhaLogin",
            placeholder = "*****",
            type= "password"
        )
        
    def Logar():
        if (UserController.UserController().logarUsuario(email, senha)):
            home.AbrirHome()
            
        else:
            print("usuario não encontrado")
            st.write("usuario não encontrado")
    
    st.button(
            label="Logar",
            key="btnLog",
            on_click=Logar,
    )

with cad:
    st.title("Cadatro")
    col1, col2= st.columns([3,1])

    with col1:
        nome = st.text_input(
            "Nome:",
            key="iptNomeCad",
            placeholder = "Carolyn W. Taylor"
            )
        email = st.text_input(
            "Email:",
            key="iptEmailCad",
            placeholder = "email@email.com"
            )
        senha = st.text_input(
            "Senha: :",
            key="iptSenhaCad",
            placeholder = "*****",
            type= "password"
        )
    def Cadastrar(nome, email, senha):
        usuario = User(nome, email, senha)
        if (UserController.cadastrarUsuario(usuario)):
            st.write("Cadastro com sucesso")
        else:
            st.write("Erro")
                
    st.button(
        label="Cadastrar",
        key="btnCad",
        on_click=Cadastrar,
        kwargs={"nome":nome, "email": email, "senha":senha}
    )


