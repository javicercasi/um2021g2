from django import forms
from .models import PublicMessageModel, PublisherModel, UserModel


class SignUpFormUser(forms.ModelForm):

    class Meta:

        model = UserModel

        fields = [
            'username',
            'firstName',
            'lastName',
            'email',
            'phone',
            'birthday',
            'bio',
            'password',
        ]

        labels = {
            'username': 'Username:',
            'firstName': 'First Name:',
            'lastName': 'Last Name:',
            'email': 'Email:',
            'phone': 'Phone:',
            'birthday': 'Birthday:',
            'bio': 'Tell me about yourself:',
            'password': 'Password:',
        }

    username = forms.CharField()
    firstName = forms.CharField()
    lastName = forms.CharField()
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


class SignInForm(forms.ModelForm):

    class Meta:

        model = UserModel

        fields = [
            'username',
            'password',
        ]

        labels = {
            'username': 'User:',
            'password': 'Password:',
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
            'text': "Whats happening?",
        }

    author = PublisherModel()
    text = forms.CharField()
