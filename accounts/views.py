from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import generics
from rest_framework.permissions import AllowAny

from accounts.serializers import RegisterSerializer


class SignUpView(generic.CreateView):
    form_class = UserCreationForm

    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
