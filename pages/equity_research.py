import streamlit as st
import pandas as pd
import yfinance as yf

from utils import get_ticker_data, chart_analyst_targets
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

# First Set of Columns
col1, col2, col3 = st.columns(3)

col1.metric("Current Price", f"${num_current_price:.2f}")
col2.metric("Analyst Rating", str_avg_analyst_rating)
col3.metric("Analyst Opinions", f"{int_analyst_opinions:.0f}")

# Second Set of Columns
delta_mean_dollar = int_target_mean_price - num_current_price
delta_mean_percent = round(delta_mean_dollar / num_current_price, 2)
delta_mean_percent = f"{delta_mean_percent:.0%}"

delta_low_dollar = int_target_low_price - num_current_price
delta_low_percent = round(delta_low_dollar / num_current_price, 2)
delta_low_percent = f"{delta_low_percent:.0%}"

delta_high_dollar = int_target_high_price - num_current_price
delta_high_percent = round(delta_high_dollar / num_current_price, 2)
delta_high_percent = f"{delta_high_percent:.0%}"

col1, col2, col3 = st.columns(3)

col1.metric("Target Low Price", f"${int_target_low_price:.2f}", delta=delta_low_percent)
col2.metric("Target Mean Price", f"${int_target_mean_price:.2f}", delta=delta_mean_percent)
col3.metric("Target High Price", f"${int_target_high_price:.2f}", delta=delta_high_percent)

st.plotly_chart(chart_analyst_targets.target_range(ticker_symbol), config={'displayModeBar': False})

##############################################################################
# Company Background

with st.expander("**Company Background**"):
    st.write(company_info.info['longBusinessSummary'])
