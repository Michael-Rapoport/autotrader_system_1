# backtesting/backtesting_engine.py
import pyfolio as pf

def backtest_strategy(strategy, data, initial_capital):
    signals = strategy(data)
    positions = signals.shift(1).fillna(0)
    
    portfolio = positions * data['close']
    portfolio['holdings'] = portfolio.sum(axis=1)
    portfolio['cash'] = initial_capital - (positions.diff().fillna(0) * data['close']).sum(axis=1).cumsum()
    portfolio['total'] = portfolio['holdings'] + portfolio['cash']
    portfolio['returns'] = portfolio['total'].pct_change()
    
    return portfolio

def analyze_performance(returns):
    performance_stats = pf.timeseries.perf_stats(returns)
    pf.create_full_tear_sheet(returns)
    return performance_stats

# backtesting/backtesting_engine.py
def backtest_strategy(strategy, data):
    signals = strategy(data)
    positions = signals.apply(lambda x: 1 if x > 0 else -1)
    returns = data['price'].pct_change() * positions.shift(1)
    cumulative_returns = (1 + returns).cumprod()
    return cumulative_returns
