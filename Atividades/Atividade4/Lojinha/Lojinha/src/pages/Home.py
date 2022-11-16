import streamlit as st
from controller.productController import productController
from models.user import User
from controller.userController import UserController

def adicionarCarrinho(idProduto):
    idProduto = int(idProduto)
    st.session_state["a"].addCarrinho(idProduto)
    
st.set_page_config(
    page_title="PokeMart",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.header("Produtos:")
poke, potion, revive = st.tabs(["PokeBall", "Potion", "Revive"])

with poke:
    st.subheader("Pokeball:")
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    
    with col1:
        st.image(
            "assets/pokeball.png",
            caption="PokeBall",
            width=200
        )
        pkball = st.button(
            '+',
            key='pkball'  ,              
            on_click = adicionarCarrinho,
            kwargs={"indice":1},  
        )
    with col2:
        st.image(
            "assets/greatball.png",
            caption="Great Ball",
            width=200
        )
        gtball = st.button(
            '+',
            key='gtball',    
            on_click = adicionarCarrinho,
            kwargs={"indice":2},  
        )
    with col3:
        st.image(
            "assets/ultraball.png",
            caption="Ultra Ball",
            width=200
        )
        utball = st.button(
            '+', 
            key='ultball',           
            on_click = adicionarCarrinho,
            kwargs={"indice":3},  
        )
    with col4:
        st.image(
            "assets/masterball.png",
            caption="Master Ball",
            width=200
        )
        mstball = st.button(
            '+', 
            key='mstball',          
            on_click = adicionarCarrinho,
            kwargs={"indice":4},  
        )
        
with potion:
    st.subheader("Potions:")
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    
    with col1:
        st.image(
            "assets/potion.png",
            caption="Potion",
            width=100
        )
        
        pot = st.button(
            '+',
            key='pt',        
            on_click = adicionarCarrinho,
            kwargs={"indice":5},  
        )
    with col2:
        st.image(
            "assets/superpotion.png",
            caption="Super Potion",
            width=100
        )
        supot = st.button(
            '+',           
            key='supot',
            on_click = adicionarCarrinho,
            kwargs={"indice":6},  
        )
    with col3:
        st.image(
            "assets/hyperpotion.png",
            caption="Hyper Potion",
            width=100
        )
        hypot = st.button(
            '+', 
            key='hypot',          
            on_click = adicionarCarrinho,
            kwargs={"indice":7},  
        )
    with col4:
        st.image(
            "assets/maxpotion.png",
            caption="Max Potion",
            width=100
        )
        maxpot = st.button(
            '+', 
            key='maxpot',       
            on_click = adicionarCarrinho,
            kwargs={"indice":8},  
        )
        
with revive:
    st.subheader("Revive:")
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(
            "assets/revive.png",
            caption="Revive",
            width=100
        )
        rev = st.button(
            '+',
            key='rev',            
            on_click = adicionarCarrinho,
            kwargs={"indice":9},  
        )
        
    with col2:
        st.image(
            "assets/maxrevive.png",
            caption="Max Revive",
            width=150
        )
        maxrev = st.button(
            '+', 
            key='maxrev',        
            on_click = adicionarCarrinho,
            kwargs={"indice":10},  
        )
    



