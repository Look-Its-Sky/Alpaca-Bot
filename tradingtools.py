import alpaca_trade_api as tradeapi

#Base info for trading only paper right now
BASE_URL = "https://paper-api.alpaca.markets"
KEY_ID = "PKD772OEONG34DX9V912"
SECRET_KEY = "kOwdXtodGbliOj2t0CDZk8objceEafUitsSveGAc"
api = tradeapi.REST(key_id=KEY_ID,secret_key=SECRET_KEY,base_url="https://paper-api.alpaca.markets")
buytype = "ioc"


def ttbuy(self, ticker, amount) -> None:
    api.submit_order(ticker, qty = amount, side = 'buy', time_in_force = buytype)   

def ttsell(self, ticker, amount) -> None:
    api.submit_order(ticker, qty = amount, side = 'sell', time_in_force = buytype)

def ttgetPostiion(self, ticker) -> float:
    return float(api.get_position(ticker).qty)

def ttGetPrice(self, ticker) -> float:
    return 

def ttCurrentPrice(self, ticker):
    return float(api.get_position(ticker).current_price)