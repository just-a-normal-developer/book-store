from django.urls import path
from .views import UserProfileView, SignUpView, UserProfileTemplateView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("template-profile/", UserProfileTemplateView.as_view(), name="user_profile_template_view"),
    path("profile/", UserProfileView.as_view(), name="user_profile"),
]
