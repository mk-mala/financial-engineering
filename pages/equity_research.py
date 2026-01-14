import streamlit as st
import pandas as pd
import yfinance as yf

from utils import get_ticker_data
from pandas.tseries.offsets import DateOffset

##############################################################################
# Sidebar

with st.sidebar:

    ticker_symbol = st.text_input(
        "Ticker Symbol",
        "MSTR",
        key="input_ticker",
    )

###############################################################################
# Input

df = get_ticker_data.price_history(ticker_symbol, period='max')

one_year_ago = pd.Timestamp.today().date() - DateOffset(years=1)
one_year_ago = one_year_ago.date()

df = df[df['Date'] >= one_year_ago]

company_info = yf.Ticker(ticker_symbol)

###############################################################################
# Company Overview

# Get Overview Data Points
str_long_name = get_ticker_data.overview(ticker_symbol, 'longName')
str_sector = get_ticker_data.overview(ticker_symbol, 'sector')
str_industry = get_ticker_data.overview(ticker_symbol, 'industry')
str_avg_analyst_rating = get_ticker_data.overview(ticker_symbol, 'averageAnalystRating')
str_exch_name = get_ticker_data.overview(ticker_symbol, 'fullExchangeName')
str_symbol = get_ticker_data.overview(ticker_symbol, 'symbol')

# Get Pricing Data Points
num_current_price = round(company_info.info['currentPrice'], 2)
int_target_low_price = round(company_info.info['targetLowPrice'], 0)
int_target_mean_price = round(company_info.info['targetMeanPrice'], 0)
int_target_high_price = round(company_info.info['targetHighPrice'], 0)
int_market_cap = round(company_info.info['marketCap'], -6)
int_analyst_opinions = round(company_info.info['numberOfAnalystOpinions'], 0)

###############################################################################
# Metrics

st.title(str_long_name)
st.write(f"{str_exch_name}: {str_symbol} | Sector: {str_sector} | Industry: {str_industry}")
