from tradingtools import *

class currency:
    ticker = ""
    
    def __init__(self, ticker) -> None:
        self.ticker = ticker

    def buy(self) -> None:
        api.submit_order(self.ticker, qty = 1, side = 'buy', time_in_force = buytype)   

    def sell(self) -> None:
        api.submit_order(self.ticker, qty = 1, side = 'sell', time_in_force = buytype)

    def getPostiion(self) -> float:
        return float(api.get_position(self.ticker).qty)