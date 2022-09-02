from bot import *
import time, threading

def main():
    threads = []
    currencies = [
        'BTCUSD',
        'ETHUSD'
    ]

    #Add different trading currencies here
    for i in currencies:
        threads.append(tradingbot(i))

    for i in threads:
        i.start()

if __name__ == "__main__":
    main()