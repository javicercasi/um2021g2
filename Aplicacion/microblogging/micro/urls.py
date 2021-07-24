from django.urls import path
from django.urls.conf import include
from .views import Home, SignUp
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('signup/', SignUp.as_view(), name='Sign Up'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]
