import streamlit as st
import pages.Home as home
import pages.Login as login
import webbrowser
import os

st.set_page_config(
    page_title="PokeMart",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title('Bem-vindo à PokeMart')

st.subheader('Sua loja Pokemon')
    
    