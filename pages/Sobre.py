# -*- coding: utf-8 -*-
"""
Created on Sat Dec 9 19:31:51 2023

@author: fariaslrc
"""

# Importando as bibliotecas
import numpy as np
import pickle
import streamlit as st

# Função para exibir a página do criador
def show_creator_page():
        

    st.title("Sobre o Cientista de Dados")
    st.write("Desenvolvido por Lucas Farias - [Linkedin](https://www.linkedin.com/in/fariaslrc/)")
    
    st.image("fariaslrc.jpg",  width=300)

show_creator_page()