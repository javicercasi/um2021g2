from django import forms
from .models import UserModel


class SignInForm(forms.ModelForm):

    class Meta:

        model = UserModel

        fields = [
            'username',
            'password',
        ]

        labels = {
            'username': 'User',
            'password': 'Password',
        }

    username = forms.CharField()
    password = forms.CharField()
