from django.db import models
from django.contrib.auth.models import AbstractUser

# auth app --> Models.User
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null = True , blank = True)

class Person(models.Model):
    username = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()