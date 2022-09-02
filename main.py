from bot import *
import time

def main():
    threads = []

    #Add different trading currencies here
    threads.append(bot('BTCUSD'))

    for i in threads:
        i.start()

if __name__ == "__main__":
    main()