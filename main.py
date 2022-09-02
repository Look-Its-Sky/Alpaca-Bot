from bot import *
import time, threading

def main():
    threads = []
    bots = []
    currencies = [
        'BTCUSD',
        'ETHUSD'
    ]

    #Add different trading currencies here
    for i in currencies:
        bots.append(tradingbot(i))

    
    for i in bots:
        threads.append(threading.Thread(target = i.run()))


    for i in threads:
        i.start()

if __name__ == "__main__":
    main()