from django.shortcuts import render
from django.views import generic
from django.contrib.auth import forms
from django.urls import reverse_lazy


class RegisterView(generic.CreateView):
    form_class = forms.UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
