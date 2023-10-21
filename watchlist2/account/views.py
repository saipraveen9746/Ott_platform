from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy



class RegitrationPage(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration.html'
