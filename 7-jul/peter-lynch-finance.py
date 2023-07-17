# 7/2 
# finance How Peter Lynch selects stocks: https://twitter.com/QCompounding/status/1675149569045176322 
# Trailing PE < 25 - Forward PE < 15 - Debt/Equity < 35% - EPS Growth > 15% - PEG Ratio < 1.2 - Market cap < $5 billion


# Import the necessary libraries
import yfinance as yf
import pandas as pd


# Define a function to calculate the PEG ratio
def calculate_peg(pe_ratio, eps_growth):
    # If eps_growth is zero, return a high number to disqualify the stock
    if eps_growth == 0:
        return 9999
    else:
        return pe_ratio / eps_growth

# Get a list of all the ticker symbols
# For this example, we'll use the S&P 500 stocks
table=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
df = table[0]
tickers = df['Symbol'].tolist()

# Filter the stocks based on the criteria
filtered_stocks = []
# for error handling
skipped_stocks = []


for ticker in tickers:
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        trailing_pe = info['trailingPE']
        forward_pe = info['forwardPE']
        debt_equity = info['debtToEquity']
        eps_growth = info['earningsQuarterlyGrowth']
        market_cap = info['marketCap']

        if trailing_pe < 25 and forward_pe < 15 and debt_equity < 0.35 and eps_growth > 0.15:
            peg_ratio = calculate_peg(trailing_pe, eps_growth)
            if peg_ratio < 1.2 and market_cap < 5000000000:
                filtered_stocks.append(ticker)
    except Exception as e:
        print(f"Could not retrieve data for {ticker}. Reason: {str(e)}")
        # add more handling logic here. add this ticker to a separate list:
        skipped_stocks.append(ticker)   


print(f"Filtered stocks: {filtered_stocks}")
