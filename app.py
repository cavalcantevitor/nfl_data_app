import streamlit as st
from menu import menu
import pandas as pd

st.set_page_config(page_title="Home")

df = pd.read_excel("data/users_scores_w1.xlsx")

st.title("BrawlZone NFL Data App")

st.header("Rankings")

st.dataframe(df)

menu()