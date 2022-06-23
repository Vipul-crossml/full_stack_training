from django.http import HttpResponse
from .models import NewProcess
from django.shortcuts import render
from .forms import NewProcessForm
# Create your views here.


def index(request):
    form = NewProcessForm()
    return render(request, "main.html",context={'form':form})



def new_process(request):
    if request.method == "POST":
        data = NewProcess()
        data.process_name = request.POST.get('process_name')   #all the get('name_field') is form html(input field - name)
        data.pipeline = request.POST.get('pipeline')
        data.classification_model = request.POST.get('classification_model')
        data.time_zone = request.POST.get('time_zone')
        data.process_sla = request.POST.get('process_sla')
        data.pre_processing = request.POST.get('pre_processing')

        data.save()
        return render(request, 'main.html')
