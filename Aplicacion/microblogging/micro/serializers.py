from rest_framework import serializers
from .models import UserModel, TagModel, PublicMessageModel


class UserSerializer(serializers.ModelSerializer):
    """ Serializador relacionado al modelo de Usuarios """

    class Meta:
        model = UserModel
        fields = ['id', 'username', 'password', 'firstName', 'lastName', 'email', 'phone', 'birthday', 'bio', 'follows', 'active']


class UserSignInSerializer(serializers.ModelSerializer):
    """ Serializador relacionado al modelo de Usuarios solo con username y password """

    class Meta:
        model = UserModel
        fields = ['username', 'password']


class TagSerializer(serializers.ModelSerializer):
    """ Serializador relacionado al modelo de Tags """

    class Meta:
        model = TagModel
        fields = ['id', 'name', 'ocurrencies']


class PublicMessageSerializer(serializers.ModelSerializer):
    """ Serializador relacionado al modelo de Mensajes publicos """

    class Meta:
        model = PublicMessageModel
        fields = ['id', 'author', 'text', 'date', 'mentions', 'tags']
