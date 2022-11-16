import streamlit as st
import controller.productController as productController
from models.user import User
import controller.userController as userController
 

# def listarCarrinho() :
#     return productController.cadas


st.set_page_config(
    page_title="PokeMart",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded",
)

compras, dadosCartao = st.columns([8,3])

with compras:
            st.header("Carrinho: ")
            # st.markdown(listarCarrinho())
            

with dadosCartao:
            st.header("Dados de Pagamento:")
            st.radio(
                'Forma de Pagamento:',
                ('Crédito', 'Débito')
            )
            st.text_input("Titular: ")
            st.text_input("CPF: ")
            st.text_input("Numero do cartão : ")
            st.text_input("CVC: ")
            st.text_input("Validade:")
            st.text_input("CEP: ")
            st.text_input("Complemento: ")
            st.button('Comprar')

