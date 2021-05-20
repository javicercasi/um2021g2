from .models import UserModel
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from .forms import SignInForm


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
                    'request': user_json.data,
                    'csrfmiddlewaretoken': data['csrfmiddlewaretoken']
                    }, status=status.HTTP_200_OK)
        return Response({
            'state': 'failure',
            'request': data,
            'error': form.errors
            }, status=status.HTTP_400_BAD_REQUEST)
