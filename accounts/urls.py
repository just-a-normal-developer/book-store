from django.urls import path
from .views import UserProfileView, SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", UserProfileView.as_view(), name="user_profile"),
]
