import streamlit as st
import pandas as pd

df_data = pd.read_csv("dataset/CLEAN_FIFA23_official_data.csv", index_col=0)
st.session_state["data"] = df_data
