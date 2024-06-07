from django.db import models
from django.contrib.auth.models import AbstractUser


# auth app --> Models.User
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)


class Person(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, verbose_name="person user"
    )
    email = models.EmailField()
