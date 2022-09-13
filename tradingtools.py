import alpaca_trade_api as tradeapi

#Base info for trading only paper right now
BASE_URL = "https://paper-api.alpaca.markets"
KEY_ID = "PKMF9F5R660ATDJD6OFL"
SECRET_KEY = "POWp5pKUxWC5keOikJXHOzyjwafYxQkXCFpdYLWZ"
api = tradeapi.REST(key_id=KEY_ID,secret_key=SECRET_KEY,base_url="https://paper-api.alpaca.markets")
#api = tradeapi.REST(key_id=KEY_ID,secret_key=SECRET_KEY,base_url="https://paper-api.alpaca.markets", api_version = 'v2')
buytype = "ioc"

def ttbuy(ticker, amount) -> None:
    api.submit_order(ticker, qty = amount, side = 'buy', time_in_force = buytype)

def ttsell(ticker, amount) -> None:
    api.submit_order(ticker, qty = amount, side = 'sell', time_in_force = buytype)

def ttgetPosition(ticker) -> float:
    return 

def ttGetPrice(ticker) -> float:
    pass

def ttCurrentPrice(self, ticker):
    return 