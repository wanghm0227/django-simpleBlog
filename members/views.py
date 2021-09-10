from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm
from django.contrib.auth.forms import UserChangeForm


class RegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class EditProfileView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
