from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), max_length=32)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), max_length=32)
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                             'class': 'form-control'}), max_length=64)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + \
            ('first_name', 'last_name', 'email',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
