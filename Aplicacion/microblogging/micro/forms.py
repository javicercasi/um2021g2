from django import forms
from .models import PublicMessageModel, UserModel


class SignUpFormUser(forms.ModelForm):

    class Meta:

        model = UserModel

        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'birthday',
            'bio',
            'password',
        ]

        labels = {
            'username': 'Username:',
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'email': 'Email:',
            'phone': 'Phone:',
            'birthday': 'Birthday:',
            'bio': 'Tell me about yourself:',
            'password': 'Password:',
        }

    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    birthday = forms.DateField()
    bio = forms.CharField()
    password = forms.CharField()


class SignUpFormCompany(forms.ModelForm):

    class Meta:

        model = UserModel

        fields = [
            'username',
            'bio',
            'password',
        ]

        labels = {
            'username': 'User:',
            'bio': 'Tell me about your company:',
            'password': 'Password:',
        }

    username = forms.CharField()
    bio = forms.CharField()
    password = forms.CharField()


class PublicMessageForm(forms.ModelForm):

    class Meta:

        model = PublicMessageModel

        fields = [
            'text',
        ]

        labels = {
            'text': "Whats happening?",
        }

    text = forms.CharField()
