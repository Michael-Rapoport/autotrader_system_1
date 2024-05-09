# execution/alpaca/alpaca_execution.py
import alpaca_trade_api as tradeapi

def execute_order(api_key, api_secret, symbol, qty, side, type, time_in_force):
    api = tradeapi.REST(api_key, api_secret, base_url='https://paper-api.alpaca.markets')
    order = api.submit_order(
        symbol=symbol,
        qty=qty,
        side=side,
        type=type,
        time_in_force=time_in_force
    )
    return order
