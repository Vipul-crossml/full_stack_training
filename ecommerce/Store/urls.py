from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', Index.as_view(), name='homepage'),
    # path('store', store, name='store'),
    path('category/', views.CategoryView.as_view()),
    path('product/', views.ProductView.as_view()),
    path('',views.index)

]
