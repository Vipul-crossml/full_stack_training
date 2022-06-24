from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import ConfigureNewProcessForm
# Create your views here.


def index(request):
    form = ConfigureNewProcessForm()
    return render(request, "main.html",context={'form':form})



def add_new_process(request):
    form=ConfigureNewProcessForm()
    print(form)
    if request.method == "POST":
        form = ConfigureNewProcessForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
        return redirect(index)
    # if request.method == "POST":
    #     data = ConfigureNewProcess()
    #     data.process_name = request.POST.get('process_name')   #all the get('name_field') is form html(input field - name)
    #     data.pipeline = request.POST.get('pipeline')
    #     data.classication_model = request.POST.get('classification_model')
    #     data.timezon = request.POST.get('timezon')
    #     data.process_sla = request.POST.get('process_sla')
    #     data.preprocessing = request.POST.get('preprocessing')

    #     data.save()
    #     return render(request, 'main.html')
