import streamlit as st
import pandas as pd
import Utils.Utils as u

u.init_page("File_upload")

file = st.file_uploader(label="Mettez votre CSV",type="csv",accept_multiple_files=False)

if file:
    data = pd.read_csv(file)
    st.text("Votre fichier, " + str(file.name) + " a été correctement importé. Voici un apperçu des données :" )
    st.dataframe(data.head())
    st.session_state["data"] = data
    st.session_state["nom_dataset"] = str(file.name).split('.')[-2]
