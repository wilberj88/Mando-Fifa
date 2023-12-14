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
club1 = st.selectbox("Club 1", clubes, index=None)

df_players1 = df_data[df_data["Club"] == club1]
players1 = df_players1["Name"].value_counts().index
player1 = st.selectbox("Jugador 1", players1, index=None)

st.header("Selecciona al jugador 2")
club2 = st.selectbox("Club 2", clubes, index=None)
df_players2 = df_data[df_data["Club"] == club2]
players2 = df_players2["Name"].value_counts().index
player2 = st.selectbox("Jugador 2", players2, index=None)


if player1 and player2:
  st.subheader("Estadísticas Jugador 1")
  player1_stats = df_data[df_data["Name"] == player1].iloc[0]
  st.image(player1_stats["Photo"])
  st.title(f"{player1_stats['Name']}")
  
  st.markdown(f"**Club:** {player1_stats['Club']}")
  st.markdown(f"**Posición:** {player1_stats['Position']}")
  
  col1, col2, col3, col4 = st.columns(4)
  col1.markdown(f"**Edad:** {player1_stats['Age']}")
  col2.markdown(f"**Altura:** {player1_stats['Height(cm.)']/100}")
  col3.markdown(f"**Peso:** {player1_stats['Weight(lbs.)']*0.453:.2f}")
  
  st.divider()
  st.subheader(f"Overal {player1_stats['Overall']}")
  st.progress(int(player1_stats['Overall']))
  
  col1, col2, col3 = st.columns(3)
  col1.metric(label="Valor de mercado", value=f"£ {player1_stats['Value(£)']:,}")
  col2.metric(label="Salario mensual", value=f"£ {player1_stats['Wage(£)']:,}")
  col3.metric(label="Cláusula de recisión", value=f"£ {player1_stats['Release Clause(£)']:,}")
    
  st.subheader("Estadísticas Jugador 2")
  player2_stats = df_data[df_data["Name"] == player2].iloc[0]
  st.image(player2_stats["Photo"])
  st.title(f"{player2_stats['Name']}")
  
  st.markdown(f"**Club:** {player2_stats['Club']}")
  st.markdown(f"**Posición:** {player2_stats['Position']}")
  
  col1, col2, col3, col4 = st.columns(4)
  col1.markdown(f"**Edad:** {player2_stats['Age']}")
  col2.markdown(f"**Altura:** {player2_stats['Height(cm.)']/100}")
  col3.markdown(f"**Peso:** {player2_stats['Weight(lbs.)']*0.453:.2f}")
  
  st.divider()
  st.subheader(f"Overal {player2_stats['Overall']}")
  st.progress(int(player2_stats['Overall']))
  
  col1, col2, col3 = st.columns(3)
  col1.metric(label="Valor de mercado", value=f"£ {player2_stats['Value(£)']:,}")
  col2.metric(label="Salario mensual", value=f"£ {player2_stats['Wage(£)']:,}")
  col3.metric(label="Cláusula de recisión", value=f"£ {player2_stats['Release Clause(£)']:,}")


  def render_basic_radar():
      option = {
              "title": {"text": "Comparativa"},
              "legend": {"data": player1_stats['Name'], player2_stats['Name']},
              "radar": {
                  "indicator": [
                      {"name": "Carbón", "max": 6500},
                      {"name": "Agua", "max": 16000},
                      {"name": "Viento", "max": 30000},
                      {"name": "Sol", "max": 38000},
                      {"name": "Petróleo", "max": 52000},
                      {"name": "Gas", "max": 25000},
                  ]
              },
              "series": [
                  {
                      "name": "Versus",
                      "type": "radar",
                      "data": [
                          {
                              "value": [6000, 10000, 20000, 3500, 15000, 11800],
                              "name": player1_stats['Name'],
                          },
                          {
                              "value": [3500, 15000, 25000, 10800, 22000, 20000],
                              "name": player2_stats['Name'],
                          },
                      ],
                  }
              ],
          }
      st_echarts(option, height="500px")
  render_basic_radar()
