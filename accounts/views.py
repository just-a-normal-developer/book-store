from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

#api's
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PersonSerializers
from .models import CustomUser


from .forms import CustomUserCreationForm
# Create your views here.

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('login')

# @api_view(['GET' , 'POST' , 'PUT'])
# def Home(request):
#     return Response({'name' : 'amir'})

class Home(APIView):
    def get(self , request):
        persons = CustomUser.objects.all()
        ser_data = PersonSerializers(instance= persons , many = True)
        return Response(data = ser_data.data)
    # def post(self , request):
    #     name = request.data['name']
    #     return Response({'name' : name , })
