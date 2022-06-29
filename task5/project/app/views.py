from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    form = ConfigureNewProcessForm()
    return render(request, "main.html", context={'form': form})


def add_new_process(request):
    form = ConfigureNewProcessForm()
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        if password==confirmpassword:
            user = User.objects.create_user(first_name=firstname, last_name=lastname,username=username,password=password)
            form = ConfigureNewProcessForm(request.POST)
            print(form.is_valid())
            if form.is_valid():
                form.save()
            return redirect(cnn)

def cnn(request):
    form = ProcessManagementForm()
    return render(request, "cnn.html",context={'form':form})

def attribute(request):
    form=ProcessManagementForm()
    if request.method == "POST" and request.FILES['file']:
        form = ProcessManagementForm(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            my_model = form.save(commit=False)
            my_model.file = request.FILES['file']
            my_model.save()
        return redirect(cnn)


        