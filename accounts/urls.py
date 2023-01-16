from django.contrib.auth import views as auth_views
from django.contrib.auth import urls as auth_urls
from django.urls import path, include
from .views import *

app_name = 'accounts'

urlpatterns = [
  path('register/', UserCreateView.as_view(), name='register'),
  path('register/done', UserCreateDoneView.as_view(), name='register_done'),
  path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  path('profile/', UserProfileView.as_view(), name='profile'),  
  path('profile/edit/', UserProfileUpdateView.as_view(), name='profile_edit'), 
  path('', include(auth_urls)),
]
