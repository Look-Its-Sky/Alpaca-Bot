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
        priceTime = takes note of the price at a certain time (used to get delta T and determine percentage change in amount of time)
        
        hasBought = was the last action the bot made a buy?
        buyPrices = prices the bot potentially should buy at

        

    """

    def __init__(self, ticker) -> None:
        threading.Thread.__init__(self)
        self.ticker = ticker

        self.terms.update(
            {
                "priceTime" : [[][]],  

                "hasBought" : False,
                "buyPrices" : [],

                "hasSold" : False,
                "sellPrices" : []
            }
        )

    def updatePrices(self):

        sellPrices = []
        buyPrices = []



        self.terms.update(
            {
                "buyPrices" : buyPrices,
                "sellPrices" : sellPrices
            }
        )

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