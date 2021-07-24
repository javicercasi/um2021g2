from datetime import datetime
from .models import FollowRelationship, PublicMessageModel, PublisherModel, UserModel
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from .serializers import PublicMessageSerializer
from .forms import SignUpFormUser, PublicMessageForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class SignUp(APIView):

    def get(self, request):
        form = SignUpFormUser()
        return render(request, "registration/signup.html", {"form": form})

    def post(self, request):
        form = SignUpFormUser(request.POST)
        if form.is_valid():
            try:
                PublisherModel.objects.get(username=form.data['username'])
            except Exception:
                user = form.save(commit=False)
                password = form.cleaned_data['password']
                user.set_password(password)
                user.save()
                return redirect('/')
        return redirect('/signup')


class Home(LoginRequiredMixin, APIView):

    def get(self, request):
        form = PublicMessageForm()
        user = request.user
        follows = FollowRelationship.objects.filter(from_user=user.id)
        all_messages = []
        own_messages = PublicMessageModel.objects.filter(author=user.id)
        for message in own_messages:
            all_messages.append(message)
        for follow in follows:
            user = UserModel.objects.get(id=follow.to_user.id)
            follow_messages = PublicMessageModel.objects.filter(author=user.id)
            for message in follow_messages:
                all_messages.append(message)
        return render(request, "index.html", {"form": form, "messages": all_messages})

    def post(self, request):
        form = PublicMessageForm(request.POST)
        if form.is_valid():
            data = {}
            data['text'] = form.data['text']
            data['date'] = datetime.now().date()
            data['author'] = request.user.id
            serializer = PublicMessageSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return redirect('/')
