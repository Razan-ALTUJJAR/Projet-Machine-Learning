import streamlit as st
import pandas as pd
import numpy as np
from Utils import Utils as u

u.init_page("pouet")

st.title('Projet streamlit groupe 3')

if("data" in st.session_state):
    data = st.session_state["data"]
    st.text("Voici les données chargées en mémoire :")
    st.dataframe(data)
else:
    st.text("Bienvenue, allez dans file upload pour charger un CSV")