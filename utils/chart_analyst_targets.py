import pandas as pd
import plotly.graph_objects as go

from utils import get_ticker_data

###############################################################################
# Functions

def target_range(ticker):

    current_price = round(get_ticker_data.overview(ticker, 'currentPrice'), 2)

    target_low_price = round(get_ticker_data.overview(ticker, 'targetLowPrice'), 2)
    target_mean_price = round(get_ticker_data.overview(ticker, 'targetMeanPrice'), 2)
    target_high_price = round(get_ticker_data.overview(ticker, 'targetHighPrice'), 2)

    df = {
        'ticker': [ticker, ticker, ticker, ticker],
        'price_type': ['Current Price', 'Low Target Price', 'Average Target Price', 'High Target Price'],
        'price_value': [current_price, target_low_price, target_mean_price, target_high_price]
    }

    df = pd.DataFrame(df)

    fig = go.Figure(
        data=[
            go.Scatter(
                x=df["price_value"],
                y=df["ticker"],
                mode="lines",
                showlegend=False,
                marker=dict(
                    color="lightgrey"
                )
            ),
            go.Scatter(
                x=df[df['price_type'] == 'Current Price']["price_value"],
                y=df[df['price_type'] == 'Current Price']["ticker"],
                mode="markers",
                name="Current Price",
                marker=dict(
                    symbol="star",
                    color="red",
                    size=10
                )
            ),
            go.Scatter(
                x=df[df['price_type'] == 'Low Target Price']["price_value"],
                y=df[df['price_type'] == 'Low Target Price']["ticker"],
                mode="markers",
                name="Low Target Price",
                marker=dict(
                    symbol="circle",
                    color="green",
                    size=10
                )
            ),
            go.Scatter(
                x=df[df['price_type'] == 'Average Target Price']["price_value"],
                y=df[df['price_type'] == 'Average Target Price']["ticker"],
                mode="markers",
                name="Average Target Price",
                marker=dict(
                    symbol="circle",
                    color="green",
                    size=10
                )
            ),
            go.Scatter(
                x=df[df['price_type'] == 'High Target Price']["price_value"],
                y=df[df['price_type'] == 'High Target Price']["ticker"],
                mode="markers",
                name="High Target Price",
                marker=dict(
                    symbol="circle",
                    color="green",
                    size=10
                )
            ),
        ]
    )

    fig.update_layout(
        autosize=False,
        height=50,
        margin=dict(t=10, b=20),
        legend_itemclick=False,
        showlegend=False,
    )

    return fig
