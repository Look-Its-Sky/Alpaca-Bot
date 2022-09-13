from datetime import *
from tradingtools import *
from threading import *

class tradingbot(Thread):

    ticker = ''
    shouldRun = True
    initBuy = 3
    position = None
    start_time = None
    last_action_time_min = None
    sellWhenPercentIsOver = 0.05
    verbose = False 

    def __init__(self, ticker) -> None:
        Thread.__init__(self);
        self.ticker = ticker
        self.position = 0

        self.start_time = datetime.now()
        
    """

    Tools

    """

    def buy(self, amount: float):
        ttbuy(self.ticker, amount)

    def sell(self, amount: float):
        ttsell(self.ticker, amount)

    """

    Trading functions

    """

    def update(self):

        self.buy(1)
        self.sell(1)

        #Sell if our coin has increased by 3% or more from our buying point
        #if self.position >= 0 and :

        #Buy if in the past couple of hours our coin has decreased by at least 3% from our selling point
        #if self.start_time < datetime.now() &&

        #Debug stuff
        if self.verbose:
            tempDict = {
                'ticker' : self.ticker,
                'shouldRun' : self.shouldRun,
                'initBuy' : self.initBuy,
                'position' : self.position,
                'start_time' : self.start_time,
                'sellWhenPercentIsOver' : self.sellWhenPercentIsOver,
            }
            print(tempDict)

    def terminate(self):
        pass

    def run(self):
        while self.shouldRun:
            self.update()
    
        if not self.shouldRun:
            self.terminate()