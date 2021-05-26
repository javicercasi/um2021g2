from datetime import datetime
from .models import PublicMessageModel, UserModel
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer, PublicMessageSerializer
from rest_framework.response import Response
from rest_framework import status
from .forms import SignInForm, PublicMessageForm


# Create your views here.
class SignUp(APIView):

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'state': 'successful',
                'request': serializer.data
                }, status=status.HTTP_200_OK)
        return Response({
            'state': 'failure',
            'request': data,
            'error': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class SignIn(APIView):

    def get(self, request):
        form = SignInForm()
        return render(request, "signin.html", {"form": form})

    def post(self, request):
        form = SignInForm(request.POST)
        data = form.data
        if form.is_valid():
            try:
                user = UserModel.objects.get(username=data['username'])
            except (Exception):
                return Response({
                    'state': 'failure'
                    }, status=status.HTTP_400_BAD_REQUEST)
            user_json = UserSerializer(user)
            if user.password == data['password']:
                return Response({
                    'state': 'successful',
                    'csrfmiddlewaretoken': data['csrfmiddlewaretoken'],
                    'request': user_json.data,
                    }, status=status.HTTP_200_OK)
        return Response({
            'state': 'failure',
            'request': data,
            'error': form.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class Feed(APIView):

    def get(self, request):
        form = PublicMessageForm()
        messages = PublicMessageModel.objects.all()
        return render(request, "feed.html", {"form": form, "messages": messages})

    def post(self, request):
        form = PublicMessageForm(request.POST)
        if form.is_valid():
            data = {}
            data['text'] = form.data['text']
            data['date'] = datetime.now().date()
            data['author'] = UserModel.objects.get(id=form.data['author']).id
            serializer = PublicMessageSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                form = PublicMessageForm()
                messages = PublicMessageModel.objects.all()
                return render(request, "feed.html", {"form": form, "messages": messages})
            return Response({
                'state': 'serializer_failure',
                'request': serializer.data,
                'error': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
                'state': 'form_failure',
                'request': form.data,
                'error': form.errors
                }, status=status.HTTP_400_BAD_REQUEST)
