from django.contrib.auth.forms import  UserCreationForm , UserChangeForm
from .models import CustomUser

#UserCreationForm --> signup
#UserChangeForm --> Admin

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age',)
        fields = ('username' , 'age', 'email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserCreationForm.Meta.fields
        fields = ('username', 'age', 'email',)



