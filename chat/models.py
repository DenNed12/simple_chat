from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    photo = models.FileField(name = 'file')


class Chat(models.Model):
   pass



