import pandas as pd
import yfinance as yf

def get_spy_data(start= "2010-01-01", end=None) -> pd.DataFrame:
    df = yf.download("SPY", start=start, end=end)
    df = df[["Open", "High", "Low", "Close", "Volume"]]
    df.dropna(inplace=True)
    return df

if __name__ == "__main__":
    spy = get_spy_data()
    print(spy.head())
