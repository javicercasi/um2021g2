from datetime import datetime
from .models import PublicMessageModel, PublisherModel, UserModel
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from .serializers import UserSerializer, PublicMessageSerializer
from rest_framework.response import Response
from rest_framework import status
from .forms import SignUpFormUser, SignInForm, PublicMessageForm


# Create your views here.
class SignUp(APIView):

    def get(self, request):
        form = SignUpFormUser()
        return render(request, "signup.html", {"form": form})

    def post(self, request):
        form = SignUpFormUser(request.POST)
        if form.is_valid():
            try:
                PublisherModel.objects.get(username=form.data['username'])
            except Exception:
                form.save()
                return redirect('/')
            return Response({
                'state': 'user_failure',
                'request': form.data,
                'error': 'User already exists'
                }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
                'state': 'form_failure',
                'request': form.data,
                'error': form.errors
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
                    'state': 'failure',
                    'error': "User doesn't exist"
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


class Home(APIView):

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
                return redirect('/')
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
