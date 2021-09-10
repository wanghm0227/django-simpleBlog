from django.contrib.auth.forms import PasswordChangeForm
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, ChangePasswordForm
from django.contrib.auth.views import PasswordChangeView


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


class ChangePassword(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'registration/change_password.html'
