from binance.client import Client
from colorama import Fore

"""
list of OHLCV values (Open time, Open, High, Low, Close, Volume, Close time, 
Quote asset volume, Number of trades, Taker buy base asset volume, Taker buy quote asset volume, Ignore)
"""

class get_historical_kandles:

    client = any
    pair_coin = 'BNBBTC'                            #Default pair_coin
    kandle_interval = Client.KLINE_INTERVAL_1HOUR   #Defaul interval time defined on client.py
    is_debug = False                                #Active/Desactive logs
    
    """ Constuctor """
    def __init__(self, client):
        self.client = client
    
    """ Example initial_date "1 Dec, 2017", finish_date: "1 Jan, 2018" """
    def get_historical_between_dates(self, pair_coin, kandle_interval, initial_date, finish_date):
        if (self.is_debug):
            print(Fore.BLUE + 'get_historical_between_dates --> DEBUG')
        return self.client.get_historical_klines(pair_coin, kandle_interval, initial_date, finish_date)
    
    """ Example time_ago: "1 day ago UTC" """
    def get_historical_from_time_ago(self, pair_coin, kandle_interval, time_ago):
        if (self.is_debug):
            print(Fore.BLUE + 'get_historical_from_time_ago --> DEBUG')
        return self.client.get_historical_klines(pair_coin, kandle_interval, time_ago)
        
    """ Change is_debug variable """
    def change_debug_status(self):
        self.is_debug = not self.is_debug
        