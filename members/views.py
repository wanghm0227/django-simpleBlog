from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm, ChangePasswordForm, ChangeSettingForm, EditProfileForm
from django.contrib.auth.views import PasswordChangeView
from .models import Profile
from django.contrib.auth.models import User


class RegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class ChangeSettingView(generic.UpdateView):
    form_class = ChangeSettingForm
    template_name = 'registration/settings.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class ChangePassword(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'registration/change_password.html'


class ShowProfileView(generic.DetailView):
    model = User
    template_name = 'registration/profile.html'


class EditProfileView(generic.UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'

    def get_object(self):
        return User.objects.get(pk=self.kwargs['pk']).profile

    def get_success_url(self):

        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})


class CreateProfileView(generic.CreateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'registration/create_profile.html'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
