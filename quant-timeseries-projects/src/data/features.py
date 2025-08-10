import pandas as pd
import numpy as np

def add_targets(df):
    #log return calc
    df['log_return'] = np.log(df['Close'] / df['Close'].shift(1))
    df['vol_park'] = np.sqrt((1/4*np.log(2))* (np.log(df['High']/ df['Low']))**2)
    return df

def make_sequences(df, feature_cols, target_col, lookback=60, horizon=1, return_index=True):
    X, y , idx = [], [], []

    #loop through the dataframe to create sequences

    sequences = []
    targets = []

    for i in range(len(df) - lookback + 1 - horizon):
        seq_x = df.iloc[i:i + lookback][feature_cols].values
        seq_y = df.iloc[i + lookback + horizon - 1][target_col]

        #sanity check for leakage
        if df.index[i + lookback + horizon - 1] <= df.index[i + lookback - 1]:
            raise ValueError("Data leakage detected: target value is from the future relative to the sequence.")

        X.append(seq_x)
        y.append(seq_y)
        if return_index:
            idx.append(df.index[i + lookback - 1])

    X = np.array(X)
    y = np.array(y)
    if return_index:
        return X, Y, pd.DatetimeIndex(idx)
    else
        return X, y

    return np.array(sequences), np.array(targets)
