import yfinance as yf

###############################################################################
# Functions

def price_history(ticker, period):
    obj_ticker = yf.Ticker(ticker) # obj_ticker = yf.Tickers(tickers)

    df = obj_ticker.history(period=period)
    df = df.reset_index()
    
    df['Date'] = df['Date'].dt.date

    if df is None:
        raise RuntimeError("YFinance returned no data.")
    
    return df


def overview(ticker, column):
    
    obj_overview = yf.Ticker(ticker)

    try:
        obj_overview.info[column]
    except:
        str_column_value = 'Not Available'
    else:
        str_column_value = obj_overview.info[column]

    return str_column_value
