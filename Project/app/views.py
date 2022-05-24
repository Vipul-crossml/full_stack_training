from tkinter.messagebox import RETRY
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "form.html")

def tables(request):
    return render(request, "tables.html")