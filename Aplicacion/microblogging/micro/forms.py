from django import forms
from .models import PublicMessageModel, PublisherModel, UserModel


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


class PublicMessageForm(forms.ModelForm):

    class Meta:

        model = PublicMessageModel

        fields = [
            'author',
            'text',
        ]

        labels = {
            'author': 'Who are you?',
            'text': "What's up?",
        }

    author = PublisherModel()
    text = forms.CharField()
