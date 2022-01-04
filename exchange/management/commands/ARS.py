from exchange.views import currency
from exchange.models import Leverage, Price , Staff,  UserInfo , Currencies , Wallet , Verify , BankCards, Transactions, Settings, Subjects, Tickets, Pages , Forgetrequest
from django.core.management.base import BaseCommand, CommandError
import requests
import time
from .lib.coinex import CoinEx

class Command(BaseCommand):
    coinex = CoinEx('130F31B38E6146DE96A96925C1238AB3', '2AA13CE30B30A1EE6798243154A4C1C5104A006BF6E8F0F8' )
    status = 'nodeal'
    coinex = CoinEx('130F31B38E6146DE96A96925C1238AB3', '2AA13CE30B30A1EE6798243154A4C1C5104A006BF6E8F0F8' )
    coin = coinex.market_ticker(market='BTCUSDT')
    averagechange = float(coin['ticker']['buy']) * 0.001
    aver = float(coin['ticker']['buy']) * 0.001
    step = averagechange
    lastprice = float(coin['ticker']['buy'])
    trades = []
    tradescount = 0
    tradesmin = 4 / float(coin['ticker']['buy'])
    def handle(self, *args, **options):
        def trader():
            while True:
                coin = self.coinex.market_ticker(market='BTCUSDT')
                price = float(coin['ticker']['buy'])
                if self.status == 'nodeal':
                    print('nodeal')
                    if price < self.lastprice - self.aver:
                        self.status = 'sdeal'
                        self.lastprice = price
                        self.tradescount = 0
                    if price > self.lastprice:
                        self.lastprice = price
                        print('raised')



                elif self.status == 'pdeal':
                    print('pdeal')
                    if price > self.lastprice + self.step:
                        
                        print('----pdeal+')
                        try:
                            self.coinex.order_market(account_id= 1 , market='BTCUSDT' , type = 'buy' , amount= 4)
                        except:
                            pass
                        self.tradescount = self.tradescount + 1
                        self.lastprice = price
                        print(self.tradescount)
                    elif price < self.lastprice - self.step:
                        print('----pdeal-')
                        for i in range(self.tradescount):
                            try:
                                self.coinex.order_market(account_id= 1 , market='BTCUSDT' , type = 'sell' , amount= self.tradesmin)
                            except:
                                pass
                        self.status = 'sdeal'
                        self.tradescount = 0


                elif self.status == 'ndeal':
                    print('ndeal')
                    if price > self.lastprice + self.step:
                        print('----ndeal+')
                        try:
                            self.coinex.order_market(account_id= 1 , market='BTCUSDT' , type = 'sell' , amount= self.tradesmin)
                        except:
                            pass
                        self.tradescount = self.tradescount + 1
                        self.lastprice = price
                        print(self.tradescount)
                    elif price < self.lastprice - self.step:
                        
                        
                        print('----ndeal-')
                        for i in range(self.tradescount):
                            try:
                                self.coinex.order_market(account_id= 1 , market='BTCUSDT' , type = 'buy' , amount= 4)
                            except:
                                pass
                        self.status = 'sdeal'
                else:


                    print('sdeal')
                    if price > self.lastprice + self.step:
                        
                        try:
                            self.coinex.order_market(account_id= 1 , market='BTCUSDT' , type = 'buy' , amount= 4)
                            self.tradescount = self.tradescount + 1
                        except:
                            pass
                        self.status = 'pdeal'
                        self.lastprice = price
                    elif price < self.lastprice:
                        self.lastprice = price
                        print('decreasde')
                time.sleep(1)
        trader()