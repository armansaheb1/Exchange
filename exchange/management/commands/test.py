from exchange.views import currency
from exchange.models import Leverage, Price , Staff,  UserInfo , Currencies , Wallet , Verify , BankCards, Transactions, Settings, Subjects, Tickets, Pages , Forgetrequest
from django.core.management.base import BaseCommand, CommandError
import requests
import time
from .lib.coinex import CoinEx

class Command(BaseCommand):
    def handle(self, *args, **options):
        coinex = CoinEx('C26DD8BAF16541E79B9526CF8CB00749', '8766839060F9FB4F34B874FD3E468C583235403E8FA4B0E8' )
        coin = coinex.balance_deposit_address_new(coin_type =  'ETH')
        print(coin)