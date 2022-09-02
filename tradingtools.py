import alpaca_trade_api as tradeapi

#Base info for trading only paper right now
BASE_URL = "https://paper-api.alpaca.markets"
KEY_ID = "PKD772OEONG34DX9V912"
SECRET_KEY = "kOwdXtodGbliOj2t0CDZk8objceEafUitsSveGAc"
api = tradeapi.REST(key_id=KEY_ID,secret_key=SECRET_KEY,base_url="https://paper-api.alpaca.markets")
buytype = "ioc"