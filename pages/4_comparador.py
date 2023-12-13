import streamlit as st

st.set_page_config(
  page_title="Comparador",
  page_icon="🔎",
  layout="wide"
)

df_data = st.session_state["data"]

st.title("Compara jugadores 🔎")
st.header("Selecciona al jugador 1")


st.header("Selecciona al jugador 2")
