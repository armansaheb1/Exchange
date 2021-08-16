from django.contrib import admin
from django.urls import path, include
from rest_framework import views
from . import views

urlpatterns = [
   path('userinfo' , views.usersinfo.as_view() , name='userinfo'),
   path('user' , views.user.as_view() , name='user'),
   path('wallet' , views.wallets.as_view() , name='wallet'),
   path('wallet/<int:id>' , views.wallet.as_view() , name='wallets'),
   path('currencies' , views.currencies.as_view() , name='Currencies'),
   path('currencies/<int:id>' , views.currency.as_view() , name='currency'),
   path('verify' , views.verify.as_view() , name='Verify'),
   path('bankcards' , views.bankcards.as_view() , name='bankcards'),
   path('bankaccounts' , views.bankaccounts.as_view() , name='bankaccounts'),
   path('transactions' , views.transactions.as_view() , name='transactions'),
   path('settings' , views.settings.as_view() , name='settings'),
   path('pages' , views.pages.as_view() , name='pages'),
   path('forget' , views.addforget.as_view() , name='addforget'),
   path('resetpass/<uuid:key>' , views.resetpass.as_view() , name='resetpass'),
   path('resetpass' , views.resetpass.as_view() , name='resetpass'),
   path('mobile-verify' , views.mobileverify.as_view() , name='mobileverify'),
   path('email-verify' , views.emailverify.as_view() , name='emailverify'),
   path('verifymelli' , views.verifymelli.as_view() , name='verifymelli'),
   path('bsc' , views.bsc.as_view() , name='bsc'),
   path('price' , views.price.as_view() , name='price'),
   path('bankrequests' , views.bankrequests.as_view() , name='bankrequests'),
   path('notifications' , views.notifications.as_view() , name='notifications'),
   path('subject' , views.subject.as_view() , name='subject'),
   path('ticket/<int:id>' , views.ticket.as_view() , name='ticket'),
   path('ticket' , views.ticket.as_view() , name='ticket'),
   path('maintrades' , views.maintrades.as_view() , name='maintrades'),
   path('protrades' , views.protrades.as_view() , name='protrades'),
   path('maintrades/<int:id>' , views.maintrades.as_view() , name='maintrades'),
   path('protrades/<int:id>' , views.protrades.as_view() , name='protrades'),
   path('fasttorial/<int:id>' , views.fasttorial.as_view() , name='fasttorial'),
   path('maintradebuyorders/<int:id>' , views.maintradebuyorders.as_view() , name='maintradebuyorders'),
   path('maintradesellorders/<int:id>' , views.maintradesellorders.as_view() , name='maintradesellorders'),
   path('maintradesinfo/<int:id>' , views.maintradesinfo.as_view() , name='maintradesinfo'),
   path('maintradesselllist' , views.maintradesselllist.as_view() , name='maintradesselllist'),
   path('maintradesbuylist' , views.maintradesbuylist.as_view() , name='maintradesbuylist'),
   
   path('protradebuyorders/<int:id>' , views.protradebuyorders.as_view() , name='protradebuyorders'),
   path('protradesellorders/<int:id>' , views.protradesellorders.as_view() , name='protradesellorders'),
   path('protradesinfo/<int:id>' , views.protradesinfo.as_view() , name='protradesinfo'),
   path('protradesselllist' , views.protradesselllist.as_view() , name='protradesselllist'),
   path('protradesbuylist' , views.protradesbuylist.as_view() , name='protradesbuylist'),

   path('fasttradesinfo/<int:id>' , views.fasttradesinfo.as_view() , name='fasttradesinfo'),
   path('dashboardinfo' , views.dashboardinfo.as_view() , name='dashboardinfo'),
   path('oltradeinfo' , views.oltradeinfo.as_view() , name='oltradeinfo'),
   path('olboardinfo' , views.olboardinfo.as_view() , name='olboardinfo'),
   path('cp_balance' , views.cp_balance.as_view() , name='cp_balance'),

   path('indexprice' , views.indexprice.as_view() , name='indexprice'),
   path('indexhistory' , views.indexhistory.as_view() , name='indexhistory'),
]
