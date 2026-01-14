import streamlit as st

# Page Configuration
st.set_page_config(page_title="Financial Engineering", layout="wide")

# Define each page
home = st.Page("pages/home.py", title="Home", icon=":material/home:")

# Create the navigation menu
pg = st.navigation([home])

# Run the selected page
pg.run()
