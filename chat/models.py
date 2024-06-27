from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    username  = models.CharField(max_length=20,default ='user')
    photo = models.ImageField(upload_to='images/', default='photo')


class Message(models.Model):
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name = 'author'
    )
    reciever = models.ForeignKey(
        to=User,
        on_delete = models.CASCADE,
        related_name = 'reciever'
    )
    content = models.CharField(max_length=300)


class Chat(models.Model):
   name = models.CharField(max_length=30, default='name')
   description = models.CharField(max_length=100,default= 'description')
   members = models.ManyToManyField(User)



