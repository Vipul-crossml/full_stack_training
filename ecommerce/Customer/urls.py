from django.contrib import admin
from django.urls import path
from .views import Signup, Login , logout


urlpatterns = [
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
]