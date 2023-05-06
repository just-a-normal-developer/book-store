from django.contrib.auth.forms import  UserCreationForm , UserChangeForm
from .models import CustomUser

#UserCreationForm --> signup
#UserChangeForm --> Admin

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields

