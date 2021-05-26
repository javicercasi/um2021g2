from django.urls import path
from .views import SignUp, SignIn, Feed


urlpatterns = [
    path('signup/', SignUp.as_view(), name='Sign Up'),
    path('signin/', SignIn.as_view(), name='Sign In'),
    path('feed/', Feed.as_view(), name='Home'),
]
