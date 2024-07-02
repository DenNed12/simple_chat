from django.contrib import admin
from chat.models import Chat, User, Message
# Register your models here.
admin.site.register(User)
admin.site.register(Chat)
admin.site.register(Message)