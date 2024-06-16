from django.http import JsonResponse
from django.views import generic
from django.urls import reverse_lazy

# api's

from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import CustomUserSerializer
from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")


class UserProfileTemplateView(generic.TemplateView):
    template_name = 'accounts/user_profile.html'
    success_url = reverse_lazy("login")


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = CustomUserSerializer(user)
        return JsonResponse(serializer.data)

    def patch(self, request):
        user = request.user
        serializer = CustomUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
