# Copyright 2023, MetaQuotes Ltd.
# https://www.mql5.com

import MetaTrader5 as mt5

mt5.initialize()


account_info = mt5.account_info()
#balance = account_info.balance
balance = 1000

symbol = "XAUUSD"
risk = 2 # percentage which you are willing to risk per trade

stop_loss_pips = 45
risk_volume = float("{:.2f}".format(balance*(risk/100)))

symbol_info = mt5.symbol_info(symbol)
symbol_info_tick = mt5.symbol_info_tick(symbol)
current_price = (symbol_info_tick.bid + symbol_info_tick.ask) / 2
pip_size = symbol_info.trade_tick_size
stop_loss = current_price - (stop_loss_pips * pip_size)

position_size = float("{:.2f}".format(risk_volume / stop_loss_pips))
if position_size >= 10:
    position_size = 10

# you code here
request_buy = {
    "action"       : mt5.TRADE_ACTION_DEAL,
    "symbol"       : symbol,
    "volume"       : position_size,
    "type"         : mt5.ORDER_TYPE_BUY,
    "price"        : mt5.symbol_info_tick(symbol).ask,
    "sl"           : stop_loss,
    "tp"           : 0.0,
    "deviation"    : 10, #integer, how many ticks are allowed for the slippage
    "magic"        : 234000, #integer, unique identifier 
    "comment"      : "python testing script",
    "type_time"    : mt5.ORDER_TIME_GTC,
    "type_filling" : mt5.ORDER_FILLING_IOC,
}

order = mt5.order_send(request_buy)

mt5.shutdown()
