from django.shortcuts import render
from rest_framework import generics
from chat.models import Message,Chat
from chat.serializers import ChatSerializer
def index(request):
    return render(request, "chat/index.html")

def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})


class ChatAPIView(generics.ListAPIView):
    queryset = Chat.objects.all()
    serializer_class =  ChatSerializer