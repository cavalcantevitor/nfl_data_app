import streamlit as st
import pandas as pd
from menu import menu

st.set_page_config(page_title="Offensive Stats")

df = pd.read_excel("data/team_offense_wk1.xlsx")

st.title("Team Offense")

st.dataframe(df)

menu()