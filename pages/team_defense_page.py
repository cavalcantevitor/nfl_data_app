import streamlit as st
import pandas as pd
from menu import menu

st.set_page_config(page_title="Defensive Stats")

df = pd.read_excel("data/team_defense_wk1.xlsx")

st.title("Team Defense")

st.dataframe(df)

menu()