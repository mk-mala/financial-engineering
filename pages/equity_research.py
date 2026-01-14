import streamlit as st

##############################################################################
# Sidebar

with st.sidebar:

    ticker_symbol = st.text_input(
        "Ticker Symbol",
        "MSTR",
        key="input_ticker",
    )
