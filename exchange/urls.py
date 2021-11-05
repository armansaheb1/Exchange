from django.contrib import admin
from django.urls import path, include
from rest_framework import views
from . import views

urlpatterns = [

#  < ------------ General
   path('review' , views.review , name='review'),
   path('timeout' , views.timeout.as_view() , name='timeout'),
   path('addphone' , views.addphone.as_view() , name='addphone'),
   path('login' , views.login.as_view() , name='mylogin'),
   path('loginsms' , views.loginsms.as_view() , name='loginsms'),
   path('welcomesms' , views.welcomesms.as_view() , name='welcomesms'),
   path('posts' , views.posts.as_view() , name='posts'),
   path('news' , views.news.as_view() , name='news'), 
   path('topsticker' , views.topsticker.as_view() , name='topsticker'), 
   path('bottomsticker' , views.bottomsticker.as_view() , name='bottomsticker'), 
   path('userinfo' , views.usersinfo.as_view() , name='userinfo'), 
   path('rulev' , views.rulev.as_view() , name='rulev'),
   path('general' , views.general.as_view() , name='general'),
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
   path('verifyaccept' , views.verifyaccept.as_view() , name='verifyaccept'),
   path('bsc' , views.bsc.as_view() , name='bsc'),
   path('price' , views.price.as_view() , name='price'),
   path('leverages' , views.leverages.as_view() , name='leverages'),
   path('pricehistory' , views.pricehistory.as_view() , name='pricehistory'),
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
   path('perpetualrequest' , views.perpetualrequest.as_view() , name='perpetualrequest'),
   path('mainpageposts' , views.mainpageposts.as_view() , name='mainpageposts'),
   path('topsticker' , views.topsticker.as_view() , name='topsticker'),
   path('bottomsticker' , views.bottomsticker.as_view() , name='bottomsticker'),
   path('otherpages' , views.otherpages.as_view() , name='otherpages'),
   path('details' , views.details.as_view() , name='details'),
   path('buy' , views.buy.as_view() , name='buy'),
   path('sell' , views.sell.as_view() , name='sell'),
   path('buyout' , views.buyout.as_view() , name='buyout'),
   path('sellout' , views.sellout.as_view() , name='sellout'),
   path('request/', views.send_request.as_view(), name='request'),
   path('<str:id>/verify/', views.verify , name='verify'),
   path('levelfee', views.levelfee.as_view() , name='levelfee'),
#  General  ------------ >   
#  < ------------ Main Trades 

   path('maintradebuyorders/<int:id>' , views.maintradebuyorders.as_view() , name='maintradebuyorders'),
   path('maintradesellorders/<int:id>' , views.maintradesellorders.as_view() , name='maintradesellorders'),
   path('maintradesinfo/<int:id>' , views.maintradesinfo.as_view() , name='maintradesinfo'),
   path('maintradesselllist' , views.maintradesselllist.as_view() , name='maintradesselllist'),
   path('maintradesbuylist' , views.maintradesbuylist.as_view() , name='maintradesbuylist'),
   
#  Main Trades  ------------ >   
#  < ------------ Pro Trades 
   
   path('protradebuyorders/<int:id>' , views.protradebuyorders.as_view() , name='protradebuyorders'),
   path('protradesellorders/<int:id>' , views.protradesellorders.as_view() , name='protradesellorders'),
   path('protradesinfo/<int:id>' , views.protradesinfo.as_view() , name='protradesinfo'),
   path('protradesselllist' , views.protradesselllist.as_view() , name='protradesselllist'),
   path('protradesbuylist' , views.protradesbuylist.as_view() , name='protradesbuylist'),

#  Pro Trades  ------------ >
#  < ------------ Dashboard Info

   path('fasttradesinfo/<int:id>' , views.fasttradesinfo.as_view() , name='fasttradesinfo'),
   path('dashboardinfo' , views.dashboardinfo.as_view() , name='dashboardinfo'),
   path('indexprice' , views.indexprice.as_view() , name='indexprice'),
   path('indexhistory' , views.indexhistory.as_view() , name='indexhistory'),

#  Dashboard Info  ------------ >
#  < ------------ Margin Trades 


   path('oltradeinfo' , views.oltradeinfo.as_view() , name='oltradeinfo'),
   path('olboardinfo' , views.olboardinfo.as_view() , name='olboardinfo'),
   path('cp_balance' , views.cp_balance.as_view() , name='cp_balance'),
   path('cp_history/<str:id>' , views.cp_history.as_view() , name='cp_history'),
   path('cp_history/' , views.cp_history.as_view() , name='cp_history'),
   path('cp_ticker' , views.cp_ticker.as_view() , name='cp_ticker'),
   path('cp_market_order' , views.cp_market_order.as_view() , name='cp_market_order'),
   path('cp_limit_order' , views.cp_limit_order.as_view() , name='cp_limit_order'),
   path('cp_stop_limit_order' , views.cp_stop_limit_order.as_view() , name='cp_stop_limit_order'),
   path('cp_cancel_order' , views.cp_cancel_order.as_view() , name='cp_cancel_order'),
   path('cp_stop_cancel_order' , views.cp_stop_cancel_order.as_view() , name='cp_stop_cancel_order'),
   path('cp_pending' , views.cp_pending.as_view() , name='cp_pending'),
   path('cp_stop_pending' , views.cp_stop_pending.as_view() , name='cp_stop_pending'),
   path('cp_close' , views.cp_close.as_view() , name='cp_close'),
   path('cp_finished' , views.cp_finished.as_view() , name='cp_finished'),
   path('cp_stop_finished' , views.cp_stop_finished.as_view() , name='cp_stop_finished'),
   path('cp_transfer' , views.cp_transfer.as_view() , name='cp_transfer'),
   path('cp_mg_transfer' , views.cp_mg_transfer.as_view() , name='cp_mg_transfer'),
   path('cp_mg_market' , views.cp_mg_market.as_view() , name='cp_mg_market'),
   path('cp_mg_usdt' , views.cp_mg_usdt.as_view() , name='cp_mg_usdt'),
   path('cp_mg_main' , views.cp_mg_main.as_view() , name='cp_mg_main'),
   path('cp_mg_settings' , views.cp_mg_settings.as_view() , name='cp_mg_settings'),
   path('cp_withdraw/<str:id>' , views.cp_withdraw.as_view() , name='cp_withdraw'),
   path('cp_deposit/<int:id>' , views.cp_deposit.as_view() , name='cp_deposit'),
   path('cp_wallets' , views.cp_wallets.as_view() , name='cp_wallets'),
   path('cp_wallet/<str:id>' , views.cp_wallet.as_view() , name='cp_wallet'),
   path('cp_currencies' , views.cp_currencies.as_view() , name='cp_address'),
   path('cp_address' , views.cp_address.as_view() , name='cp_currencies'),
   path('cp_currencies/<str:id>' , views.cp_currency.as_view() , name='cp_currency'),
#  Margin Trades  ------------ >


#  < ------------ Perpetual Trades 


   path('olpmarketinfo' , views.olpmarketinfo.as_view() , name='olpmarketinfo'),
   path('olptradeinfo' , views.olptradeinfo.as_view() , name='olptradeinfo'),
   path('olpboardinfo' , views.olpboardinfo.as_view() , name='olpboardinfo'),
   path('cpp_adjustleverage' , views.cpp_adjustleverage.as_view() , name='cpp_adjustleverage'),
   path('cpp_balance' , views.cpp_balance.as_view() , name='cpp_balance'),
   path('cpp_market_order' , views.cpp_market_order.as_view() , name='cpp_market_order'),
   path('cpp_limit_order' , views.cpp_limit_order.as_view() , name='cpp_limit_order'),
   path('cpp_stop_limit_order' , views.cpp_stop_limit_order.as_view() , name='cpp_stop_limit_order'),
   path('cpp_cancel_order' , views.cpp_cancel_order.as_view() , name='cpp_cancel_order'),
   path('cpp_pending' , views.cpp_pending.as_view() , name='cpp_pending'),
   path('cpp_stop_pending' , views.cpp_stop_pending.as_view() , name='cpp_stop_pending'),
   path('cpp_close' , views.cpp_close.as_view() , name='cpp_close'),
   path('cpp_finished' , views.cpp_finished.as_view() , name='cpp_finished'),
   path('cpp_stop_finished' , views.cpp_stop_finished.as_view() , name='cpp_stop_finished'),


#  Perpetual Trades  ------------ >


]