from django.urls import path , include
from . import views

urlpatterns = [
    path('signup/' , views.SignUpView.as_view() , name = 'signup'),
    path('home/', views.Home.as_view(), name="api-test"),

]
