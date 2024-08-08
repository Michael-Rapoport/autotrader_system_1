import pandas as pd

def momentum_strategy(data, lookback_period):
    data['momentum'] = data['close'].pct_change(lookback_period)
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0
    signals['signal'][data['momentum'] > 0] = 1
    signals['signal'][data['momentum'] < 0] = -1
    return signals