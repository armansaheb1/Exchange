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
    coin = coinex.market_ticker(market='SOLUSDT')
    averagechange = float(coin['ticker']['buy']) * 0.001
    step = averagechange
    lastprice = 0
    trades = []
    tradescount = 0
    tradesmin = 4 / float(coin['ticker']['buy'])
    def handle(self, *args, **options):
        def trader():
            while True:
                coin = self.coinex.market_ticker(market='SOLUSDT')
                price = float(coin['ticker']['buy'])



                if self.status == 'nodeal':
                    print('nodeal')
                    self.status = 'sdeal'
                    self.lastprice = price
                    self.tradescount = 0



                elif self.status == 'pdeal':
                    print('pdeal')
                    if price > self.lastprice + self.step:
                        
                        print('----pdeal+')
                        if self.tradescount < 5:
                            try:
                                self.coinex.order_market(account_id= 76 , market='SOLUSDT' , type = 'buy' , amount= 4)
                            except:
                                pass
                            self.tradescount = self.tradescount + 1
                            self.lastprice = price
                            print(self.tradescount)
                    elif price < self.lastprice - self.step:
                        print('----pdeal-')
                        for i in range(self.tradescount):
                            try:
                                self.coinex.order_market(account_id= 76 , market='SOLUSDT' , type = 'sell' , amount= self.tradesmin)
                            except:
                                pass
                        self.status = 'nodeal'


                elif self.status == 'ndeal':
                    print('ndeal')
                    if price > self.lastprice + self.step:
                        print('----ndeal+')
                        if self.tradescount < 5:
                            try:
                                self.coinex.order_market(account_id= 76 , market='SOLUSDT' , type = 'sell' , amount= self.tradesmin)
                            except:
                                pass
                            self.tradescount = self.tradescount + 1
                            self.lastprice = price
                            print(self.tradescount)
                    elif price < self.lastprice - self.step:
                        
                        
                        print('----ndeal-')
                        for i in range(self.tradescount):
                            try:
                                self.coinex.order_market(account_id= 76 , market='SOLUSDT' , type = 'buy' , amount= 4)
                            except:
                                pass
                        self.status = 'nodeal'
                else:


                    print('sdeal')
                    if price > self.lastprice + self.step:
                        
                        try:
                            self.coinex.order_market(account_id= 76 , market='SOLUSDT' , type = 'buy' , amount= 4)
                            self.tradescount = self.tradescount + 1
                        except:
                            pass
                        self.status = 'pdeal'
                        self.lastprice = price
                time.sleep(1)
        trader()