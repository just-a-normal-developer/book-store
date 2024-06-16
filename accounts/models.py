from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser


# auth app --> Models.User
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)

    def clean(self):
        if self.age < 18:
            raise ValidationError("age can not be under 18")
