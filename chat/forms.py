from django import forms
from models import User, Chat, Message

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields  = ['content']


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['name']