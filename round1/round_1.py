from datamodel import OrderDepth, UserId, TradingState, Order
from typing import List

class Products:
    RAINFOREST_RESIN = "RAINFOREST_RESIN"
    KELP = "KELP"
    SQUID_INK = "SQUID_INK"

class Trader:
    def run(self, state: TradingState):
        result = {}
        order_depth: OrderDepth = state.order_depths[Products.RAINFOREST_RESIN] 
        orders: list[Order] = []

        upper_bound = 10003.8
        lower_bound = 9995.9

        if len(order_depth.sell_orders) != 0 and len(order_depth.buy_orders) != 0:
            best_ask = min(order_depth.sell_orders.keys())
            best_ask_volume = order_depth.sell_orders[best_ask]
            best_bid = max(order_depth.buy_orders.keys())
            best_bid_volume = order_depth.buy_orders[best_bid]

            mid_price = (best_ask + best_bid) / 2

            if mid_price > upper_bound:
                print("SELL", str(best_bid_volume) + "x", best_bid)
                orders.append(Order(Products.RAINFOREST_RESIN, best_bid, -best_bid_volume))

            elif mid_price < lower_bound:
                print("BUY", str(-best_ask_volume) + "x", best_ask)
                orders.append(Order(Products.RAINFOREST_RESIN, best_ask, -best_ask_volume)) 
            else:
                print("NO ACTION")

        result[Products.RAINFOREST_RESIN] = orders

        traderData = "SAMPLE" 
        
        conversions = 1 
        
        return result, conversions, traderData

            

        




