from django import forms
from .models import ConfigureNewProcess, ProcessManagement
# Create your forms here.


class ConfigureNewProcessForm(forms.ModelForm):
    process_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = ConfigureNewProcess
        fields = '__all__'


class ProcessManagementForm(forms.ModelForm):
    class Meta:
        model = ProcessManagement
        exclude = ["file"]
