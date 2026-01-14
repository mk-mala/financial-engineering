import streamlit as st

# Page Configuration
st.set_page_config(page_title="Financial Engineering", layout="wide")

# Define each page
home = st.Page("pages/home.py", title="Home", icon=":material/home:")
equity_research = st.Page("pages/equity_research.py", title="Equity Research", icon=":material/article:")

# Create the navigation menu
pg = st.navigation([home, equity_research])

# Run the selected page
pg.run()
