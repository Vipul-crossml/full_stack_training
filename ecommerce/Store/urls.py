from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('store', store , name='store'),
    path('category/', views.CategoryView.as_view()),
    path('product/', views.ProductView.as_view()),
    path('login/', views.login, name='login'),
    path('Signup/', views.signup, name='Signup'),
    path('',views.index)

]
