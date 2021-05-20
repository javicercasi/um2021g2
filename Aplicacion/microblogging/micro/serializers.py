from rest_framework import serializers
from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    """ Serializador relacionado al modelo de Usuarios """

    class Meta:
        model = UserModel
        fields = ['id', 'username', 'password', 'firstName', 'lastName', 'email', 'phone', 'birthday', 'bio', 'active']


class UserSignInSerializer(serializers.ModelSerializer):
    """ Serializador relacionado al modelo de Usuarios solo con username y password """

    class Meta:
        model = UserModel
        fields = ['username', 'password']
