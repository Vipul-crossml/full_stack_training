from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_new_process', views.add_new_process, name='add_new_process'),
]