import streamlit as st

st.set_page_config(
  page_title="Players",
  page_icon="🏃",
  layout="wide"
)

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Club", clubes)

df_players = df_data[df_data["Club"] == club]
players = df_data["Name"].value_counts().index
player = st.sidebar.selectbox("Jugador", players)

player_stats = df_data[df_data["Name"] == player].iloc[0]

st.image(player_stats["Photo"])
st.title(f"{player_stats["Name"]}")

st.markdown(f"**Club:** {player_stats['Club']}")
st.markdown(f"**Posición:** {player_stats['Position']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Edad:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)']/100}")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)']*0.453:.2f}")

st.divider()
st.subheader(f"Overal {player_stast['Overall']}")
st.progress(int(player_stats['Overall']))

col1, col2, col3 = st.columns(3)
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="Salario mensual", value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de recisión", value=f"£ {player_stats['Release Clause(£)']:,}")


