import streamlit as st

st.set_page_config(
  page_title="Comparador",
  page_icon="🔎",
  layout="wide"
)

df_data = st.session_state["data"]
clubes = df_data["Club"].value_counts().index



st.title("Compara jugadores 🔎")
st.header("Selecciona al jugador 1")
club1 = st.selectbox("Club 1", clubes)

df_players1 = df_data[df_data["Club"] == club1]
players1 = df_players1["Name"].value_counts().index
player1 = st.selectbox("Jugador 1", players1)

st.header("Selecciona al jugador 2")
club2 = st.selectbox("Club 2", clubes)
df_players2 = df_data[df_data["Club"] == club2]
players2 = df_players2["Name"].value_counts().index
player2 = st.selectbox("Jugador 2", players2)
