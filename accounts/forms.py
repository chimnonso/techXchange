from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class UserCreateForm(UserCreationForm):
    password1 = forms.CharField(label='Password', 
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', 
                                widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        help_texts = {
            'username': None,
        }