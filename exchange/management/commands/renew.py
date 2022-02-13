from exchange.models import Perpetual, Staff,  UserInfo , Currencies , Wallet , Verify , BankCards, Transactions, Settings, Subjects, Tickets, Pages , Forgetrequest
import requests
from bit import Key
from django.core.management.base import BaseCommand, CommandError
from cryptos import *
from .lib import CoinexPerpetualApi

class Command(BaseCommand):
    def handle(self, *args, **options):
        for item in Perpetual.objects.all():
            robot = CoinexPerpetualApi(item.apikey, item.secretkey)

            result = robot.apis()
            print(result)