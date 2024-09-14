import streamlit as st

def menu():
    # Show navigation bar
    st.sidebar.page_link("app.py", label="Rankings")
    st.sidebar.page_link("pages/team_offense_page.py", label="Offensive Stats")
    st.sidebar.page_link("pages/team_defense_page.py", label="Defensive Stats")