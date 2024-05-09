# risk_management/position_sizing.py
def fixed_fraction_position_sizing(account_balance, risk_per_trade):
    position_size = account_balance * risk_per_trade
    return position_size
