from datetime import date, datetime
from tradingtools import *
import threading, time

def bot(Thread):

    ticker = ''
    shouldRun = True
    initialBuy = 75000 #How much of an asset to buy in USD (only bought once the program is run and if there is not a position in this asset)
    terms = {}

    """

    ticker = the ticker of the coin
    shouldRun = controls when the bot should terminate
    initialBuy = how much of the coin the bot should buy on initialize if a position isnt already held
    terms = conditions on which the bot should buy and sell
        prices & time = takes note of the price at a certain time
                        (used to get delta T and determine percentage change in amount of time)
                        the list positions correlate to each other
        
        buyPrices = prices the bot potentially should buy at
        sellPrices = prices the bot should potentially sell at
                     arranged from worst case sceneraio to best case scenerio
                     it sells 5% of the current position for every milestone hit
                     until the current position doesnt hold enough to sell anymore (user defined)
        
    percentUpSell = by how much the price of the coin should rise before it the bot should sell by one milestone
    percentDownBuy = by how much the price of the coin should dip before the bot should buy in again

    """

    def __init__(self, ticker) -> None:
        threading.Thread.__init__(self)
        self.ticker = ticker

        self.terms.update(
            {
                "prices" : [],
                "time" : [],
                "lastAction" : "",  
                "buyPrices" : [],
                "sellPrices" : [],
                "percentChange" : 0.05
            }
        )

    """
    Get current price of the coin
    """

    def currentPrice() -> float:
        return ttCurrentPrice(ticker)

    """"
    Buy function
    """

    def buy(self, amountInUSD: float):
        amount = amountInUSD / currentPrice()
        ttbuy(ticker, amount)

    def sell(self, amountInUSD: float):
        amount = amountInUSD / currentPrice()

    """
    Get difference between two times
    """

    def getDeltaT(self, date1, date2):
        return date1 - date2

    def shouldSell(self) -> bool:
        for i in range(len(self.terms.get("prices"))):
            percentChange = 1 + self.terms.get("percentChange")
            
            if self.terms.get("prices")[i] * percentChange <= self.terms.get("prices")[-1]:
               return True
        
        return False

    def shouldBuy(self) -> bool:
        for i in range(len(self.terms.get("prices"))):
            percentChange = 1 - self.terms.get("percentChange")
            
            if self.terms.get("prices")[i] * percentChange >= self.terms.get("prices")[-1]:
               return True
        
        return False

    """
    Get the amount of time it took to accomplish your selling point
    The amount of time it took to increase <desired percent> at which the bot sold at
    """
    def getTimeTakenForMilestone(self):
        for i in range(len(self.terms.get("prices"))):
            if shouldSell():
                return i * 5 #Goal met

        return -1 #Goal not met

    """
    Update terms dictonary
    """
    def updatePrices(self):
        pass

    #Put algorithmic stuff here
    def update(self):
        pass


    #On terminate
    def terminate(self):
        pass

    def run(self):
        while self.shouldRun:
            update()
    
        if not self.shouldRun:
            terminate()