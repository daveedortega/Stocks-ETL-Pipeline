## SCRIPT TO GET THE HISTORICAL DATA
# DAOA
# 19/08/2025

## Setup: 
import pandas as pd
import numpy as np
import yfinance as yf

## Declare portfolio: 
big_tech = {
    "AAPL": "Apple Inc.",
    "MSFT": "Microsoft Corporation", 
    "GOOGL": "Alphabet Inc. (Google) - Class A",
    "GOOG": "Alphabet Inc. (Google) - Class C",
    "TSLA": "Tesla Inc.",
    "AMZN": "Amazon.com Inc.",
    "META": "Meta Platforms Inc. (Facebook)",
    "NVDA": "NVIDIA Corporation", 
    "PYPL": "PayPal Holdings",
    "UBER": "Uber Technologies",
    "NFLX": "Netflix Inc.",
    "ORCL": "Oracle Corporation",
    "CRM": "Salesforce Inc.",
    "ADBE": "Adobe Inc.",
    "INTC": "Intel Corporation",
    "AMD": "Advanced Micro Devices",
    "CSCO": "Cisco Systems Inc.",
    "IBM": "International Business Machines",
    "QCOM": "QUALCOMM Incorporated",
    "TXN": "Texas Instruments",
    "TSM": "Taiwan Semiconductor",     # World's largest chip manufacturer
    "ARM": "Arm Holdings",            # CPU architecture (recent IPO)
}

indexes = {
    "^GSPC": "S&P 500",              # Market benchmark
    "^VIX": "Volatility Index",       # Fear gauge
    "^IXIC": "NASDAQ Composite",     # Tech-heavy index
    "^MXX": "Mexico's top stock"
}

major_banks = {
    "JPM": "JPMorgan Chase & Co.",                  # Largest US bank
    "BAC": "Bank of America Corp.",                 # Consumer banking giant
    "C": "Citigroup Inc.",                          # Global banking
    "GS": "Goldman Sachs Group",                    # Investment banking
    "MS": "Morgan Stanley",                         # Wealth management
    "COF": "Capital One Financial",                 # Credit cards/digital banking
    "BBVA": "Global BBVA", 
    "GFNORTEO.MX": "Banorte", 
    "DBK.DE": "Deutsche Bank"
}

fintech_stocks = {
    "PYPL": "PayPal Holdings",                      # You already have this
    "MA": "Mastercard Inc.",                        # Payment networks
    "V": "Visa Inc.",                               # Payment networks
    "AXP": "American Express Co."                  # Premium cards/payments
}

major_mexican = {
    "AMX":    "América Móvil",                       # Largest telecom in LatAm
    "BIMBOA.MX":  "Grupo Bimbo",                         # Global bakery leader
    "CEMEXCPO.MX": "Cemex",                              # Cement & construction
    "GMEXICOB.MX": "Grupo México",                       # Mining & infrastructure
    "WALMEX.MX":  "Walmart de México",                   # Retail giant
    #"KOFL.MX":    "Coca-Cola FEMSA",                     # Coke bottler
    "KIMBERA.MX": "Kimberly-Clark de México",            # Consumer products
    "ALSEA.MX":   "Alsea",                               # Restaurants operator
    "GCARSOA1.MX": "Grupo Carso",                        # Carlos Slim’s conglomerate
}

## Declare df:
stock_df = pd.DataFrame()

## BIG TECH
for symbol in big_tech.keys():
    print(f"Fetching {symbol}...")
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period='max', interval='1d')
    
    # Create DataFrame with date as a column
    tmp_df = pd.DataFrame({
        'Stock': symbol,
        'Date': hist.index,  # ← This was missing!
        'Open': hist['Open'],
        'High': hist['High'],    # ← Add this for better analysis
        'Low': hist['Low'],      # ← Add this too
        'Close': hist['Close'],
        'Volume': hist['Volume'], 
        'Type': 'Big Tech'
    })
    
    stock_df = pd.concat([stock_df, tmp_df], ignore_index=True)
print('Done')

## INDICES
for symbol in indexes.keys():
    print(f"Fetching {symbol}...")
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period='max', interval='1d')
    
    # Create DataFrame with date as a column
    tmp_df = pd.DataFrame({
        'Stock': symbol,
        'Date': hist.index,  # ← This was missing!
        'Open': hist['Open'],
        'High': hist['High'],    # ← Add this for better analysis
        'Low': hist['Low'],      # ← Add this too
        'Close': hist['Close'],
        'Volume': hist['Volume'], 
        'Type': 'Indexes'
    })
    
    stock_df = pd.concat([stock_df, tmp_df], ignore_index=True)
print('Done')

## BANKING
for symbol in major_banks.keys():
    print(f"Fetching {symbol}...")
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period='max', interval='1d')
    
    # Create DataFrame with date as a column
    tmp_df = pd.DataFrame({
        'Stock': symbol,
        'Date': hist.index,  # ← This was missing!
        'Open': hist['Open'],
        'High': hist['High'],    # ← Add this for better analysis
        'Low': hist['Low'],      # ← Add this too
        'Close': hist['Close'],
        'Volume': hist['Volume'], 
        'Type': 'Major Banks'
    })
    
    stock_df = pd.concat([stock_df, tmp_df], ignore_index=True)
print('Done')


## FINTECH
for symbol in fintech_stocks.keys():
    print(f"Fetching {symbol}...")
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period='max', interval='1d')
    
    # Create DataFrame with date as a column
    tmp_df = pd.DataFrame({
        'Stock': symbol,
        'Date': hist.index,  # ← This was missing!
        'Open': hist['Open'],
        'High': hist['High'],    # ← Add this for better analysis
        'Low': hist['Low'],      # ← Add this too
        'Close': hist['Close'],
        'Volume': hist['Volume'], 
        'Type': 'Fintech'
    })
    
    stock_df = pd.concat([stock_df, tmp_df], ignore_index=True)
print('Done')


## MEXICAN STOCKS
for symbol in major_mexican.keys():
    print(f"Fetching {symbol}...")
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period='max', interval='1d')
    
    # Create DataFrame with date as a column
    tmp_df = pd.DataFrame({
        'Stock': symbol,
        'Date': hist.index,  # ← This was missing!
        'Open': hist['Open'],
        'High': hist['High'],    # ← Add this for better analysis
        'Low': hist['Low'],      # ← Add this too
        'Close': hist['Close'],
        'Volume': hist['Volume'], 
        'Type': 'Major Mexican'
    })
    
    stock_df = pd.concat([stock_df, tmp_df], ignore_index=True)
print('Done')

# Add calculations
stock_df['Daily_Change'] = ((stock_df['Close'] - stock_df['Open']) / stock_df['Open']) * 100
stock_df['Daily_Range'] = ((stock_df['High'] - stock_df['Low']) / stock_df['Open']) * 100
stock_df['Daily_Return'] = stock_df.groupby('Stock')['Close'].pct_change() * 100
stock_df['Volatility_20d'] = stock_df.groupby('Stock')['Daily_Return'].transform(
    lambda x: x.rolling(window=20, min_periods=5).std()
)

print(stock_df.head())
