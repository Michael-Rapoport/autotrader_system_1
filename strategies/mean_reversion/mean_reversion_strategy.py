# strategies/mean_reversion/mean_reversion_strategy.py
import pandas as pd

def mean_reversion_strategy(data, lookback_period, entry_threshold, exit_threshold):
    data['z_score'] = (data['close'] - data['close'].rolling(lookback_period).mean()) / data['close'].rolling(lookback_period).std()
    
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0
    
    signals['signal'][data['z_score'] < -entry_threshold] = 1
    signals['signal'][data['z_score'] > entry_threshold] = -1
    signals['signal'][data['z_score'] > -exit_threshold] = 0
    signals['signal'][data['z_score'] < exit_threshold] = 0
    
    return signals

