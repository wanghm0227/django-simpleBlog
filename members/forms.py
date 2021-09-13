from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                             'class': 'form-control'}))

    class Meta():
        model = User
        fields = UserCreationForm.Meta.fields + \
            ('first_name', 'last_name', 'email',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})


class ChangeSettingForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                             'class': 'form-control'}))

    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', ]


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))


class EditProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}), required=False)
    profile_pic = forms.ImageField(widget=forms.ClearableFileInput(
        attrs={'class': 'form-control'}), label='Profile picture', required=False)
    website_url = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), required=False)
    facebook_url = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'}), required=False)
    twitter_url = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'}), required=False)
    instagram_url = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'}), required=False)

    class Meta():
        model = Profile
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.use_required_attribute = False
