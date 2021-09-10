from django import forms
from .models import Post, Category

CHOICES = [cat for cat in Category.objects.all().values_list('name', 'name')]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author', 'likes']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=CHOICES, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


