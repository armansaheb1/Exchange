from exchange import serializers
from exchange.lib import request_client
from django.shortcuts import render
from django.contrib.auth import get_user_model

from exchange.models import LevelFee , UserInfo
from .models import (
    ChatSession, ChatSessionMessage, User, deserialize_user
)
from exchange.serializers import AdminChatSerializer, LevelFeeSerializer
from rest_framework import status
from rest_framework import authentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from ippanel import Client

def sms(user , date = False , text = False , pattern = 'gf9zbtg61v'):
    sms = Client("qsVtNKDEKtFZ9wgS4o1Vw81Pjt-C3m469UJxCsUqtBA=")

    if pattern == 'r4hxan3byx' or pattern == 'tfpvvl8beg'  :
        pattern_values = {
    "text": text,
    }
    else :
        pattern_values = {
    "name": "کاربر",
    }

    bulk_id = sms.send_pattern(
        f"{pattern}",    # pattern code
        "+983000505",      # originator
        f"+98{UserInfo.objects.get(user = user).mobile}",  # recipient
        pattern_values,  # pattern values
    )

    message = sms.get_message(bulk_id)
    print(message)
    print(f"+98999999999")
    return True

class ChatSessionView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication ]
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """create a new chat session."""
        if not 'email' in request.data:
            user = request.user
        else: 
            email= request.data['email']
        if not 'email' in request.data:
            chats =  ChatSession.objects.filter(owner = request.user)
        else:
            chats =  ChatSession.objects.filter(email = email)
        for item in chats :
            item.delete()
        if not 'email' in request.data:
            chat_session = ChatSession.objects.create(owner=user)
        else:
            chat_session = ChatSession.objects.create(email=email)
        ChatSessionMessage.objects.create(
                    email='کارشناس', chat_session=chat_session, message='به پشتیبانی آمیزاکس خوش آمدید , چطور میتونم کمکتون کنم؟', aseen=True , admin= True
                )
        return Response({
            'status': 'SUCCESS', 'uri': chat_session.uri,
            'message': 'New chat session created'
        })
    
    def patch(self, request, *args, **kwargs):
        """Add a user to a chat session."""
        
        return Response ({
            'status': 'SUCCESS',
        })


class ChatSessionMessageView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication ]
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        """return all messages in a chat session."""
        uri = kwargs['uri']

        chat_session = ChatSession.objects.get(uri=uri)
        messages = [chat_session_message.to_json() 
            for chat_session_message in chat_session.messages.all().order_by('id')]
        notseen = 0
        for item in chat_session.messages.all():
            if not item.seen:
                notseen = notseen + 1
        return Response({
            'id': chat_session.id, 'uri': chat_session.uri,
            'messages': messages, 'notseen' : notseen
        })

    def post(self, request, *args, **kwargs):
        """create a new message in a chat session."""
        uri = kwargs['uri']
        message = request.data['message']
        if not 'email' in request.data:
            user = request.user
        else: 
            email= request.data['email']
        chat_session = ChatSession.objects.get(uri=uri)
            
        if not 'email' in request.data:
            ChatSessionMessage.objects.create(
                user=user, chat_session=chat_session, message=message, seen=True , admin= False
            )
        else:
            ChatSessionMessage.objects.create(
                email=email, chat_session=chat_session, message=message, seen=True , admin= False
            )
        sms(user = User.objects.get(id = 1) ,text= 'پیام جدید در چت سایت', pattern= 'gn4mg2t2ulyjkn0')
        if not 'email' in request.data:
            return Response ({
                'status': 'SUCCESS', 'uri': chat_session.uri, 'message': message,
                'user': deserialize_user(user)
            })
        return Response ({
            'status': 'SUCCESS', 'uri': chat_session.uri, 'message': message,
            'user': email
        })

class ChatSessionMessageViewAdmin(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication ]
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """create a new message in a chat session."""
        uri = kwargs['uri']
        message = request.data['message']
        if not 'email' in request.data:
            user = request.user
        else: 
            email= request.data['email']
        chat_session = ChatSession.objects.get(uri=uri)
            
        if not 'email' in request.data:
            ChatSessionMessage.objects.create(
                user=user, chat_session=chat_session, message=message, aseen=True , admin= True
            )
        return Response ({
            'status': 'SUCCESS', 'uri': chat_session.uri, 'message': message,
            'user': email
        })

class user(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication ]
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        user = ChatSession.objects.get(email = request.data['email'])
        return Response({'uri' : user.uri , 'username' : user.email})

    def get(self, request, *args, **kwargs):
        user = ChatSession.objects.get(owner = request.user)
        return Response({'uri' : user.uri , 'username' : request.user.username})

class seen(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication ]
    permission_classes = [AllowAny]
    def get(self, request, uri, *args, **kwargs):
        if request.user.is_staff:
            chat_session = ChatSession.objects.get(uri=uri)
            messages = chat_session.messages.all()
            for item in messages:
                item.aseen = True
                item.save()
            return Response(True)
        chat_session = ChatSession.objects.get(uri=uri)
        messages = chat_session.messages.all()
        for item in messages:
            item.seen = True
            item.save()
        return Response(True)

class adminchat(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, authentication.TokenAuthentication ]
    permission_classes = [AllowAny]
    
    def get(self, request, *args, **kwargs):
        user = ChatSession.objects.all()
        serializer = AdminChatSerializer(user , many=True)
        return Response(serializer.data)


