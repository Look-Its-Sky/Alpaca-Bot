import alpaca_trade_api as tradeapi

#Base info for trading only paper right now
BASE_URL = "https://paper-api.alpaca.markets"
KEY_ID = "PKNQ638MQIWY658JF8UY"
SECRET_KEY = "xLlFt1iGRy9f0wY1wp9V7O4gVTP2Z1wtslTiKELg"
api = tradeapi.REST(key_id=KEY_ID,secret_key=SECRET_KEY,base_url="https://paper-api.alpaca.markets")
buytype = "ioc"
current_position = 0

def ttbuy(ticker, amount) -> None:
    api.submit_order(ticker, qty = amount, side = 'buy', time_in_force = buytype)
    current_position += amount

def ttsell(ticker, amount) -> None:
    api.submit_order(ticker, qty = amount, side = 'sell', time_in_force = buytype)
    current_position -= amount

def ttgetPostion(ticker) -> float:
    return current_position
    #return float(api.get_position(ticker).qty) API ERROR smh

def ttGetPrice(ticker) -> float:
    pass

def ttCurrentPrice(ticker):
    return float(api.get_position(ticker).current_price)