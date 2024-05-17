import streamlit as st
# from utils import PrepProcesor

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import joblib

# model = joblib.load('xgbpipe.joblib')

st.title("Application d'une Distribution Normale :ship:")
st.subheader("Auteur : Riton")
st.write("Cette application permet d'afficher l'histogramme d'une distribution normale.")
st.markdown("***L'utilisateur peut modifier le nombre de bins ainsi que le titre du graphe***")
data = np.random.normal(size=1000)
data = pd.DataFrame(data, columns=["Dist_norm"])
st.write(data.head())
fig, ax = plt.subplots()
n_bins = st.number_input(
       label="Choisis un nb de bins",
       min_value=10,
       value=20
       )
       
ax.hist(data.Dist_norm, bins=n_bins)
graph_title = st.text_input(
       label="Donner le titre du graphique"
       )
# st.set_option('deprecation.showPyplotGlobalUse', False)
plt.title(graph_title)
st.pyplot(fig)

st.line_chart(data)
bar_data = pd.DataFrame(
    [100, 29, 56, 34],
    ["A", "B", "C", "D"]
    )
st.bar_chart(bar_data)

