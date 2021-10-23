from typing import Text
from django.utils import timezone
from django.db.models import manager
from exchange.views import cp_withdraw, currencies, currency, notifications, price, usersinfo
from django.shortcuts import get_object_or_404, render
from django import http
from django.db.models.fields import EmailField
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from rest_framework import request, serializers
from django.http import HttpResponse , Http404 
from rest_framework import status
from rest_framework import authentication
from exchange.serializers import  BottomStickerSerializer, BuySerializer, BuyoutSerializer, Cp_WithdrawSerializer, CpWalletSerializer, GeneralSerializer, LevelFeeSerializer, PerpetualRequestSerializer, PostsSerializer, SellSerializer, TopStickerSerializer, VerifyMelliRequest , BankAccountsSerializer, StaffSerializer, UserInfoSerializer, VerifyBankAccountsRequestSerializer, VerifyMelliRequestSerializer , WalletSerializer , CurrenciesSerializer ,VerifySerializer, BankCardsSerializer, TransactionsSerializer, SettingsSerializer, SubjectsSerializer, TicketsSerializer, PagesSerializer , UserSerializer , ForgetSerializer, VerifyBankRequestSerializer, selloutSerializer
from rest_framework.views import APIView 
from rest_framework.response import Response
from exchange.models import BottomSticker, Cp_Withdraw, General, LevelFee, News, Notification, Perpetual, PerpetualRequest, Posts ,  Price, Review, Staff, TopSticker,  UserInfo , Currencies, VerifyAcceptRequest, VerifyBankAccountsRequest, VerifyBankRequest, VerifyMelliRequest , Wallet , Verify , BankCards, Transactions, Settings, Subjects, Tickets, Pages , Forgetrequest, buyoutrequest, buyrequest, selloutrequest, sellrequest
from django.contrib.auth.models import AbstractUser , User
from django.contrib.auth.decorators import user_passes_test
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from py_crypto_hd_wallet import HdWalletFactory, HdWalletCoins, HdWalletSpecs , HdWalletWordsNum
import json
from datetime import datetime ,timedelta
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from ippanel import Client
import pytz
from random import randrange
from django.db.models import Q

def email(user , date , title , text) :
    send_mail(
        'Subject here',
        f'به شرکت سرمایه گذاری ... خوش آمدید کد فعالسازی : {"vcode"} ',
        'info@ramabit.com',
        [f'armansaheb@gmail.com'],
        fail_silently=False,
    )

def sms(user , date , title  , text ):
    sms = Client("qsVtNKDEKtFZ9wgS4o1Vw81Pjt-C3m469UJxCsUqtBA=")

    pattern_values = {
    "verification-code": f"dcsdcdscd",
    }

    bulk_id = sms.send_pattern(
        "nyxequ9zz4",    # pattern code
        "+983000505",      # originator
        f"+98{UserInfo.objects.get(user = user).mobile}",  # recipient
        pattern_values,  # pattern values
    )

    message = sms.get_message(bulk_id)
    print(message)
    print(f"+98999999999")
    return True

def notification (user , date = datetime.now(), title = '' , text = ''):
    note = Notification(user = user , title = title , text = text)
    note.save()
    sms(user , date, title, text)
    email(user , date, title, text)

class staff(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication ]
    permission_classes = [IsAuthenticated]

    def get_object(self , user):
        try:
            return Staff.objects.filter(user = user)
        except UserInfo.DoesNotExist:
            return Http404

    def get(self , request , format=None):
        if len(self.get_object(request.user)) < 1 :
            return Response(status=status.HTTP_400_BAD_REQUEST)
        staff =  self.get_object(request.user)
        serializer = StaffSerializer(staff , many=True)
        return Response(serializer.data)

    def post(self , request , format=None):
        if Staff.objects.get(user = request.user).level < 3 :
            return Response(status= status.HTTP_400_BAD_REQUEST)
        if len(Staff.objects.filter(user = request.user))<1:
            serializer = StaffSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.error, status= status.HTTP_400_BAD_REQUEST)
        else:
            serializer = Staff.objects.get(user = request.data['id'])
            serializer.level = request.data['level']
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class user(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication ]
    permission_classes = [IsAuthenticated]

    def get(self , request ,user, format=None):
        if len(Staff.objects.filter(user = request.user))<1:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            if Staff.objects.get(user = request.user).level < 1 :
                return Response(status= status.HTTP_400_BAD_REQUEST)
        users = []
        userinfo =  User.objects.filter(username=user)
        for item in userinfo :
            if len(UserInfo.objects.filter(user = item)) > 0:
                userinfos = UserInfo.objects.get(user = item)
                wallet= 0
                price = 0
                for itemm in Wallet.objects.filter(user = item):
                    if itemm.currency.id == 1:
                        price = 1
                    elif itemm.currency.id == 2:
                        price = Price.objects.get(id = 1).btc * Price.objects.get(id = 1).usd
                    elif itemm.currency.id == 3:
                        price = Price.objects.get(id = 1).eth * Price.objects.get(id = 1).usd
                    elif itemm.currency.id == 4:
                        price = Price.objects.get(id = 1).usdt * Price.objects.get(id = 1).usd
                    elif itemm.currency.id == 5:
                        price = Price.objects.get(id = 1).trx * Price.objects.get(id = 1).usd
                    elif itemm.currency.id == 6:
                        price = Price.objects.get(id = 1).doge * Price.objects.get(id = 1).usd
                    wallet = wallet + (itemm.amount * price)
                users.append({'username': item.username, 'level': userinfos.level, 'balance': wallet, 'is_active': userinfos.is_active, 'is_admin': item.is_staff, 'id': item.id })
        return Response(users)
    def post(self , request , format=None):
        user = UserInfo.objects.get(user = User.objects.get(id = request.data['id']))
        if request.data['act'] == 1:
            if user.is_active == True:
                user.is_active = False
            elif user.is_active == False:
                user.is_active = True
        user.save()
        return Response(status=status.HTTP_201_CREATED)

class users(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication ]
    permission_classes = [IsAuthenticated]

    def get(self , request , format=None):
        if len(Staff.objects.filter(user = request.user))<1:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            if Staff.objects.get(user = request.user).level < 1 :
                return Response(status= status.HTTP_400_BAD_REQUEST)
        users = []
        userinfo =  User.objects.all()
        for item in userinfo :
            if len(UserInfo.objects.filter(user = item)) > 0:
                userinfos = UserInfo.objects.get(user = item)
                wallet= 0
                price = 0
                for itemm in Wallet.objects.filter(user = item):
                    if itemm.currency.id == 1:
                        price = 1
                    elif itemm.currency.id == 2:
                        price = Price.objects.get(id = 1).btc * Price.objects.get(id = 1).usd
                    elif itemm.currency.id == 3:
                        price = Price.objects.get(id = 1).eth * Price.objects.get(id = 1).usd
                    elif itemm.currency.id == 4:
                        price = Price.objects.get(id = 1).usdt * Price.objects.get(id = 1).usd
                    elif itemm.currency.id == 5:
                        price = Price.objects.get(id = 1).trx * Price.objects.get(id = 1).usd
                    elif itemm.currency.id == 6:
                        price = Price.objects.get(id = 1).doge * Price.objects.get(id = 1).usd
                    wallet = wallet + (itemm.amount * price)
                users.append({'username': item.username, 'level': userinfos.level, 'balance': wallet, 'is_active': userinfos.is_active, 'is_admin': item.is_staff, 'id': item.id })
        return Response(users)
    def post(self , request , format=None):
        user = UserInfo.objects.get(user = User.objects.get(id = request.data['id']))
        if request.data['act'] == 1:
            if user.is_active == True:
                user.is_active = False
            elif user.is_active == False:
                user.is_active = True
        user.save()
        return Response(status=status.HTTP_201_CREATED)

class bankcards(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication ]
    permission_classes = [IsAuthenticated]

    def get(self , request , format=None):
        if len(Staff.objects.filter(user = request.user))<1:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            if Staff.objects.get(user = request.user).level < 1 :
                return Response(status= status.HTTP_400_BAD_REQUEST)
        bankcards = VerifyBankRequest.objects.all()
        serializer = VerifyBankRequestSerializer(bankcards , many=True)
        return Response(serializer.data)

    def post(self , request , format=None):
        if len(Staff.objects.filter(user = request.user))<1:
            return Response({'message': 'not admin'}, status= status.HTTP_400_BAD_REQUEST)
        else:
            if Staff.objects.get(user = request.user).level < 1 :
                return Response({'message': 'not admin'}, status= status.HTTP_400_BAD_REQUEST)
        request.data['user'] = VerifyBankRequest.objects.get(id = request.data['id']).user.id
        serializer = BankCardsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            VerifyBankRequest.objects.get(id = request.data['id']).delete()
            verify = Verify.objects.get(user = request.data['user'])
            verify.bankv = True
            verify.save()
            if verify.bankv and verify.melliv and verify.mobilev and verify.emailv and verify.acceptv and verify.coinv and verify.accontv :
                user = UserInfo.objects.get(user = request.data['user'])
                user.level = 1
                user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self , request , format=None):
        if len(Staff.objects.filter(user = request.user))<1:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            if Staff.objects.get(user = request.user).level < 1 :
                return Response(status= status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        req = VerifyBankRequest.objects.get(id = id)
        req.delete()
        return Response(status=status.HTTP_201_CREATED)

class bankaccounts(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication ]
    permission_classes = [IsAuthenticated]

    def get(self , request , format=None):
        if len(Staff.objects.filter(user = request.user))<1:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            if Staff.objects.get(user = request.user).level < 1 :
                return Response(status= status.HTTP_400_BAD_REQUEST)
        bankcards = VerifyBankAccountsRequest.objects.all()
        serializer = VerifyBankAccountsRequestSerializer(bankcards , many=True)
        return Response(serializer.data)

    def post(self , request , format=None):
        if len(Staff.objects.filter(user = request.user))<1:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            if Staff.objects.get(user = request.user).level < 1 :
                return Response(status= status.HTTP_400_BAD_REQUEST)
        serializer = BankAccountsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            id = request.data['id']
            req = VerifyBankAccountsRequest.objects.get(id = id)
            ver = Verify.objects.get(user = req.user)
            ver.accountv = True
            ver.save()
            verify = Verify.objects.get(user = req.user)
            if verify.bankv and verify.melliv and verify.mobilev and verify.emailv and verify.acceptv and verify.coinv and verify.accontv :
                user = UserInfo.objects.get(user = req.user)
                user.level = 1
                user.save()
            req = VerifyBankAccountsRequest.objects.get(id = id)
            req.delete()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self , request , format=None):
        if len(Staff.objects.filter(user = request.user))<1:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            if Staff.objects.get(user = request.user).level < 1 :
                return Response(status= status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        req = VerifyBankAccountsRequest.objects.get(id = id)
        req.delete()
        return Response(status=status.HTTP_201_CREATED)

class verifymelli(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication ]
    permission_classes = [IsAuthenticated]

    def get(self , request , format=None):
        if len(Staff.objects.filter(user = request.user))<1:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            if Staff.objects.get(user = request.user).level < 1 :
                return Response(status= status.HTTP_400_BAD_REQUEST)
        bankcards = VerifyMelliRequest.objects.all()
        serializer = VerifyMelliRequestSerializer(bankcards , many=True)
        return Response(serializer.data)

    def post(self , request , format=None):
        if len(Staff.objects.filter(user = request.user))<1:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            if Staff.objects.get(user = request.user).level < 1 :
                return Response(status= status.HTTP_400_BAD_REQUEST)
        verify = Verify.objects.get(user = request.data['user'])
        verify.melliv = True
        verify.save()
        if verify.bankv and verify.melliv and verify.mobilev and verify.emailv and verify.acceptv and verify.coinv and verify.accontv :
            user = UserInfo.objects.get(user = request.data['user'])
            user.level = 1
            user.save()
        id = request.data['id']
        req = VerifyMelliRequest.objects.get(id = id)
        req.act = True
        req.save()
        return Response(status=status.HTTP_201_CREATED)
 
class verifyaccept(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication ]
    permission_classes = [IsAuthenticated]

    def get(self , request , format=None):
        if len(Staff.objects.filter(user = request.user))<1:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            if Staff.objects.get(user = request.user).level < 1 :
                return Response(status= status.HTTP_400_BAD_REQUEST)
        bankcards = VerifyAcceptRequest.objects.all()
        serializer = VerifyBankAccountsRequestSerializer(bankcards , many=True)
        return Response(serializer.data)

    def post(self , request , format=None):
        if len(Staff.objects.filter(user = request.user))<1:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            if Staff.objects.get(user = request.user).level < 1 :
                return Response(status= status.HTTP_400_BAD_REQUEST)
        verify = Verify.objects.get(user = request.data['user'])
        verify.acceptv = True
        verify.save()
        if verify.bankv and verify.melliv and verify.mobilev and verify.emailv and verify.acceptv and verify.coinv and verify.accontv :
                user = UserInfo.objects.get(user = request.data['user'])
                user.level = 1
                user.save()
        id = request.data['id']
        req = VerifyAcceptRequest.objects.get(id = id)
        req.act = True
        req.save()
        return Response(status=status.HTTP_201_CREATED)


    def put(self , request , format=None):
        if len(Staff.objects.filter(user = request.user))<1:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            if Staff.objects.get(user = request.user).level < 1 :
                return Response(status= status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        req = VerifyAcceptRequest.objects.get(id = id)
        req.delete()
        return Response(status=status.HTTP_201_CREATED)


class cwithdraw(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication ]
    permission_classes = [IsAuthenticated]

    def get(self , request , format=None):
        if len(Staff.objects.filter(user = request.user))<1:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            if Staff.objects.get(user = request.user).level < 1 :
                return Response(status= status.HTTP_400_BAD_REQUEST)
        bankcards = Cp_Withdraw.objects.filter(rejected = False , completed = False)
        serializer = Cp_WithdrawSerializer(bankcards , many=True)
        return Response(serializer.data)

    def post(self , request , format=None):
        if len(Staff.objects.filter(user = request.user))<1:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            if Staff.objects.get(user = request.user).level < 1 :
                return Response(status= status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        req = Cp_Withdraw.objects.get(id = id)
        user = req.user.id
        notification(user = User.objects.get(id = user) , title = 'درخواست برداشت وجه شما انجام شد' , text = f'درخواست برداشت مقدار  {req.amount} و ارسال آن به آدرس  {req.address} با موفقیت انجام شد ')
        req.completed = True
        req.save()
        return Response(status=status.HTTP_201_CREATED)
 
    def put(self , request , format=None):
        if len(Staff.objects.filter(user = request.user))<1:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            if Staff.objects.get(user = request.user).level < 1 :
                return Response(status= status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        req = Cp_Withdraw.objects.get(id = id)
        user = req.user.id
        notification(user = User.objects.get(id = user) , title = ' متاسفانه درخواست برداشت وجه شما انجام نشد ' , text = f'درخواست برداشت مقدار  {req.amount} و ارسال آن به آدرس  {req.address}  با مشکل روبرو شد . لطفا با پشتیبانی تماس بگیرید ')
        req.rejected = True
        req.save()
        return Response(status=status.HTTP_201_CREATED)

class rcwithdraw(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication ]
    permission_classes = [IsAuthenticated]

    def get(self , request , format=None):
        if len(Staff.objects.filter(user = request.user))<1:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            if Staff.objects.get(user = request.user).level < 1 :
                return Response(status= status.HTTP_400_BAD_REQUEST)
        bankcards = Cp_Withdraw.objects.filter(rejected = True)
        serializer = Cp_WithdrawSerializer(bankcards , many=True)
        return Response(serializer.data)

class ccwithdraw(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication ]
    permission_classes = [IsAuthenticated]

    def get(self , request , format=None):
        if len(Staff.objects.filter(user = request.user))<1:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            if Staff.objects.get(user = request.user).level < 1 :
                return Response(status= status.HTTP_400_BAD_REQUEST)
        bankcards = Cp_Withdraw.objects.filter(completed = True)
        serializer = Cp_WithdrawSerializer(bankcards , many=True)
        return Response(serializer.data)


class general(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication ]
    permission_classes = [IsAuthenticated]

    def get(self , request , format=None):
        if len(Staff.objects.filter(user = request.user))<1:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            if Staff.objects.get(user = request.user).level < 1 :
                return Response(status= status.HTTP_400_BAD_REQUEST)
        query = General.objects.filter(id = 1)
        serializer = GeneralSerializer(query , many=True)
        return Response(serializer.data)

    def post(self , request , format=None):
        if len(Staff.objects.filter(user = request.user))<1:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            if Staff.objects.get(user = request.user).level < 1 :
                return Response(status= status.HTTP_400_BAD_REQUEST)
        gen = General.objects.get(id = 1)
        if 'name' in request.data :
            gen.name = request.data['name']
        if 'email' in request.data :
            gen.email = request.data['email']
        if 'telephone' in request.data :
            gen.telephone = request.data['telephone']
        if 'instagram' in request.data :
            gen.instagram = request.data['instagram']
        if 'telegram' in request.data :
            gen.telegram = request.data['telegram']
        if 'whatsapp' in request.data :
            gen.whatsapp = request.data['whatsapp']
        if 'rule' in request.data :
            gen.rule = request.data['rule']
        if 'logo' in request.data :
            gen.logo = request.data['logo']
        gen.save()
        return Response(status=status.HTTP_201_CREATED)

class perpetualreq(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication ]
    permission_classes = [IsAuthenticated]

    def get(self , request , format=None):
        if len(Staff.objects.filter(user = request.user))<1:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            if Staff.objects.get(user = request.user).level < 1 :
                return Response(status= status.HTTP_400_BAD_REQUEST)
        query = PerpetualRequest.objects.all()
        serializer = PerpetualRequestSerializer(query , many=True)
        return Response(serializer.data)

    def post(self , request, id , format=None):
        if len(Staff.objects.filter(user = request.user))<1:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            if Staff.objects.get(user = request.user).level < 1 :
                return Response(status= status.HTTP_400_BAD_REQUEST)
        query = PerpetualRequest.objects.filter(id = id)
        serializer = PerpetualRequestSerializer(query , many=True)
        return Response(serializer.data)

class perpetualreqccept(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication ]
    permission_classes = [IsAuthenticated]

    def post(self , request , format=None):
        if len(Staff.objects.filter(user = request.user))<1:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            if Staff.objects.get(user = request.user).level < 1 :
                return Response(status= status.HTTP_400_BAD_REQUEST)
        id = request.data['id']
        user = PerpetualRequest.objects.get(id = id).user
        print(request.data['name'])
        per = Perpetual(user = user ,name = request.data['name'], apikey = request.data['apikey'] , secretkey = request.data['secretkey'])
        per.save()
        ver = Verify.objects.get(user = user)
        ver.coinv = True
        ver.save()
        verify = Verify.objects.get(user = user)
        if verify.bankv and verify.melliv and verify.mobilev and verify.emailv and verify.acceptv and verify.coinv and verify.accontv :
                user = UserInfo.objects.get(user = user)
                user.level = 1
                user.save()
        PerpetualRequest.objects.get(id = id).delete()
        return Response(status=status.HTTP_201_CREATED)


class subject(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication ]
    permission_classes = [IsAuthenticated]
    
    def get_object(self , user):
        return Subjects.objects.all()

    def get(self , request , format=None):
        if len(Staff.objects.filter(user = request.user))<1:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            if Staff.objects.get(user = request.user).level < 1 :
                return Response(status= status.HTTP_400_BAD_REQUEST)

        if len(self.get_object(request.user)) < 1 :
            return Response(status=status.HTTP_400_BAD_REQUEST)
        userinfo =  self.get_object(request.user)
        serializer = SubjectsSerializer(userinfo , many=True)
        return Response(serializer.data)

    def post(self, request, id, format=None):
        if len(Staff.objects.filter(user = request.user))<1:
            return Response(status= status.HTTP_400_BAD_REQUEST)
        else:
            if Staff.objects.get(user = request.user).level < 1 :
                return Response(status= status.HTTP_400_BAD_REQUEST)

        if len(self.get_object(request.user)) < 1 :
            return Response(status=status.HTTP_400_BAD_REQUEST)
        userinfo =  Subjects.objects.filter(id = id)
        serializer = SubjectsSerializer(userinfo , many=True)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        request.data['user'] = User.objects.get(username = request.data['username']).id
        sub = Subjects(user = request.user , title = request.data['title'])
        sub.save()
        request.data['user'] = request.user.id
        request.data['subid'] = sub.id
        serializer = TicketsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ticket(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication ]
    permission_classes = [IsAuthenticated]
    
    def get_object(self , id):
        return Tickets.objects.filter(subid = id)

    def get(self , request , id , format=None):
        if len(self.get_object(id)) < 1 :
            return Response(status=status.HTTP_400_BAD_REQUEST)
        userinfo =  self.get_object(id)
        serializer = TicketsSerializer(userinfo , many=True)
        return Response(serializer.data)

    def post(self , request , format=None):
        request.data['user'] = request.user.id
        serializer = TicketsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class topsticker(APIView):
    def get(self , request , format=None):
        pages = Pages.objects.filter(position = 'top')
        serializer = PagesSerializer(pages , many=True)
        return Response(serializer.data)

    def post(self , request , format=None):
        serializer = PagesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    def delete(self , request, id, format=None):
        serializer = Pages.objects.get(id = id)
        serializer.delete()
        return Response(status=status.HTTP_201_CREATED)

    def put(self , request , format=None):
        post = Pages.objects.get(id=request.data['id'])
        post.text = request.data['text']
        post.minitext = request.data['minitext']
        post.title = request.data['title']
        if 'pic' in request.data:
            print(request.data)
            post.pic = request.data['pic']
        post.save()
        return Response(status=status.HTTP_201_CREATED)

class bottomsticker(APIView):
    def get(self , request , format=None):
        pages = Pages.objects.filter(position = 'bottom')
        serializer = PagesSerializer(pages , many=True)
        return Response(serializer.data)
        
    def post(self , request , format=None):
        serializer = PagesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    def delete(self , request, id, format=None):
        serializer = Pages.objects.get(id = id)
        serializer.delete()
        return Response(status=status.HTTP_201_CREATED)

    def put(self , request , format=None):
        post = Pages.objects.get(id=request.data['id'])
        post.text = request.data['text']
        post.minitext = request.data['minitext']
        post.title = request.data['title']
        if 'pic' in request.data:
            print(request.data)
            post.pic = request.data['pic']
        post.save()
        return Response(status=status.HTTP_201_CREATED)


class mainpageposts(APIView):
    def get(self , request , format=None):
        pages = Pages.objects.filter(position = 'mainposts')
        serializer = PagesSerializer(pages , many=True)
        return Response(serializer.data)
        
    def post(self , request , format=None):
        serializer = PagesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    def delete(self , request, id, format=None):
        serializer = Pages.objects.get(id = id)
        serializer.delete()
        return Response(status=status.HTTP_201_CREATED)

    def put(self , request , format=None):
        post = Pages.objects.get(id=request.data['id'])
        post.text = request.data['text']
        post.minitext = request.data['minitext']
        post.title = request.data['title']
        if 'pic' in request.data:
            print(request.data)
            post.pic = request.data['pic']
        post.save()
        return Response(status=status.HTTP_201_CREATED)


class otherpages(APIView):
    def get(self , request , format=None):
        pages = Pages.objects.filter(position = 'others')
        serializer = PagesSerializer(pages , many=True)
        return Response(serializer.data)
        
    def post(self , request , format=None):
        serializer = PagesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    def delete(self , request, id, format=None):
        serializer = Pages.objects.get(id = id)
        serializer.delete()
        return Response(status=status.HTTP_201_CREATED)

    def put(self , request , format=None):
        post = Pages.objects.get(id=request.data['id'])
        post.text = request.data['text']
        post.minitext = request.data['minitext']
        post.title = request.data['title']
        if 'pic' in request.data:
            print(request.data)
            post.pic = request.data['pic']
        post.save()
        return Response(status=status.HTTP_201_CREATED)


class wallets(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication ]
    permission_classes = [IsAuthenticated]

    def get_object(self , user):
        try:
            return Wallet.objects.filter(user = User.objects.get(username= user))
        except Wallet.DoesNotExist:
            return Http404
            
    def get(self , request, username , format=None):
        userinfo = self.get_object(user = username)
        serializer = WalletSerializer(userinfo , many=True)
        return Response(serializer.data)


class levelchange(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication ]
    permission_classes = [IsAuthenticated]
            
    def post(self , request , format=None):
        userinfo = UserInfo.objects.get(user = User.objects.get(username = request.data['username']))
        userinfo.level = int(request.data['level'])
        userinfo.save()
        return Response(status=status.HTTP_201_CREATED)
        

class changepass(APIView):
    def post(self , request):
        user = User.objects.get(username = request.data['username'])
        passw = request.data['pass']
        passs = make_password(str(passw))
        user.password = passs
        user.save()
        return Response(status=status.HTTP_201_CREATED)

class review(APIView):
    def get(self, request):
        hours = 0
        days = 0
        weeks = 0
        months = 0
        for item in Review.objects.all():
            if item.date > timezone.now() - timedelta(hours = 1):
                hours = hours + 1
            if item.date > timezone.now() - timedelta(days = 1):
                days = days + 1
            if item.date > timezone.now() - timedelta(weeks = 1):
                weeks = weeks + 1
            if item.date > timezone.now() - timedelta(weeks = 4):
                months = months + 1
        return Response({'days': days,'weeks': weeks, 'months': months, 'hours': hours })


class buy(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication ]
    permission_classes = [IsAuthenticated]
    
    def get_object(self, user):
        return buyrequest.objects.filter(act = 0).order_by('-date')

    def get(self , request, format=None):
        maintrade =  self.get_object(request.user)
        serializer = BuySerializer(maintrade , many=True)
        return Response(serializer.data , status=status.HTTP_201_CREATED)

    def post(self , request, format=None):
        if request.data['act'] == 'reject':
            req = buyrequest.objects.get(id = request.data['id'])
            note = Notification(user=req.user, title = 'خرید نا موفق' , text = 'متاسفانه درخواست خرید شما با مشکل مواجه شده . لطفا با پشتیبانی تماس بگیرید')
            note.save()
            req.act = 1
            req.save()
            return Response(status=status.HTTP_201_CREATED)
        req = buyrequest.objects.get(id = request.data['id'])
        note = Notification(user=req.user, title = 'خرید موفق' , text = ' درخواست خرید شما با موفقیت انجام شد . ')
        note.save()
        req.act = 2
        req.save()
        return Response( status=status.HTTP_201_CREATED)

class buyout(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication ]
    permission_classes = [IsAuthenticated]
    
    def get_object(self, user):
        return buyoutrequest.objects.filter(act = 0).order_by('-date')

    def get(self , request, format=None):
        maintrade =  self.get_object(request.user)
        serializer = BuyoutSerializer(maintrade , many=True)
        return Response(serializer.data , status=status.HTTP_201_CREATED)

    def post(self , request, format=None):
        if request.data['act'] == 'reject':
            req = buyoutrequest.objects.get(id = request.data['id'])
            note = Notification(user=req.user, title = 'خرید نا موفق' , text = 'متاسفانه درخواست خرید شما با مشکل مواجه شده . لطفا با پشتیبانی تماس بگیرید')
            note.save()
            req.act = 1
            req.save()
            return Response(status=status.HTTP_201_CREATED)
        req = buyoutrequest.objects.get(id = request.data['id'])
        note = Notification(user=req.user, title = 'خرید موفق' , text = ' درخواست خرید شما با موفقیت انجام شد . ')
        note.save()
        req.act = 2
        req.save()
        return Response( status=status.HTTP_201_CREATED)

class sellout(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication ]
    permission_classes = [IsAuthenticated]
    
    def get_object(self, user):
        return selloutrequest.objects.filter(act = 0).order_by('-date')

    def get(self , request, format=None):
        maintrade =  self.get_object(request.user)
        serializer = selloutSerializer(maintrade , many=True)
        return Response(serializer.data , status=status.HTTP_201_CREATED)

    def post(self , request, format=None):
        if request.data['act'] == 'reject':
            req = selloutrequest.objects.get(id = request.data['id'])
            note = Notification(user=req.user, title = 'خرید نا موفق' , text = 'متاسفانه درخواست خرید شما با مشکل مواجه شده . لطفا با پشتیبانی تماس بگیرید')
            note.save()
            req.act = 1
            req.save()
            return Response(status=status.HTTP_201_CREATED)
        req = selloutrequest.objects.get(id = request.data['id'])
        note = Notification(user=req.user, title = 'خرید موفق' , text = ' درخواست خرید شما با موفقیت انجام شد . ')
        note.save()
        req.act = 2
        req.save()
        return Response( status=status.HTTP_201_CREATED)

class selloutopen(APIView):
    def get_object(self, user):
        return selloutrequest.objects.filter(act = 0).order_by('-date')

    def get(self , request, format=None):
        maintrade =  self.get_object(request.user)
        serializer = selloutSerializer(maintrade , many=True)
        return Response(serializer.data , status=status.HTTP_201_CREATED)
class buyoutopen(APIView):
    def get_object(self, user):
        return buyoutrequest.objects.filter(act = 0).order_by('-date')

    def get(self , request, format=None):
        maintrade =  self.get_object(request.user)
        serializer = BuyoutSerializer(maintrade , many=True)
        return Response(serializer.data , status=status.HTTP_201_CREATED)

class sellouthistory(APIView):
    def get_object(self, user):
        return selloutrequest.objects.filter(~Q(act = 0)).order_by('-date')

    def get(self , request, format=None):
        maintrade =  self.get_object(request.user)
        serializer = selloutSerializer(maintrade , many=True)
        return Response(serializer.data , status=status.HTTP_201_CREATED)

class buyouthistory(APIView):
    def get_object(self, user):
        return buyoutrequest.objects.filter(~Q(act = 0)).order_by('-date')

    def get(self , request, format=None):
        maintrade =  self.get_object(request.user)
        serializer = BuyoutSerializer(maintrade , many=True)
        return Response(serializer.data , status=status.HTTP_201_CREATED)



class sellopen(APIView):
    def get_object(self, user):
        return sellrequest.objects.filter(act = 0).order_by('-date')

    def get(self , request, format=None):
        maintrade =  self.get_object(request.user)
        serializer = SellSerializer(maintrade , many=True)
        return Response(serializer.data , status=status.HTTP_201_CREATED)
class buyopen(APIView):
    def get_object(self, user):
        return buyrequest.objects.filter(act = 0).order_by('-date')

    def get(self , request, format=None):
        maintrade =  self.get_object(request.user)
        serializer = BuySerializer(maintrade , many=True)
        return Response(serializer.data , status=status.HTTP_201_CREATED)

class sellhistory(APIView):
    def get_object(self, user):
        return sellrequest.objects.filter(~Q(act = 0)).order_by('-date')

    def get(self , request, format=None):
        maintrade =  self.get_object(request.user)
        serializer = SellSerializer(maintrade , many=True)
        return Response(serializer.data , status=status.HTTP_201_CREATED)
class buyhistory(APIView):
    def get_object(self, user):
        return buyrequest.objects.filter(~Q(act = 0)).order_by('-date')

    def get(self , request, format=None):
        maintrade =  self.get_object(request.user)
        serializer = BuySerializer(maintrade , many=True)
        return Response(serializer.data , status=status.HTTP_201_CREATED)



class levelfee(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication ]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        user = LevelFee.objects.all().order_by('id')
        serializer = LevelFeeSerializer(user , many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = LevelFee.objects.get(id = request.data['id'])
        serializer.buy = request.data['buy']
        serializer.sell = request.data['sell']
        serializer.perpetual = request.data['perpetual']
        serializer.margin = request.data['margin']
        serializer.exchange = request.data['exchange']
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)