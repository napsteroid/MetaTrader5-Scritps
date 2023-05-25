# Copyright 2023, MetaQuotes Ltd.
# https://www.mql5.com

import MetaTrader5 as mt5

mt5.initialize()

positions = mt5.positions_get()
#print(positions)

if positions == ():
    print("There is nothing to close.")
    exit()

symbol = positions[0].symbol
volume = positions[0].volume
ticket = positions[0].ticket
order_type = positions[0].type  # 0 for buy and 1 for sell

if(order_type == 0):
    order_type = mt5.ORDER_TYPE_SELL
    price = mt5.symbol_info_tick(symbol).bid
else:
    order_type = mt5.ORDER_TYPE_BUY
    price = mt5.symbol_info_tick(symbol).ask

close_request={
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": float(volume),
    "type": order_type,
    "position": ticket,
    "price": price,
    "magic": 234000,
    "comment": "Close trade",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_IOC,
}

order = mt5.order_send(close_request)

mt5.shutdown()
