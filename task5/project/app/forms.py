from django import forms
from .models import ConfigureNewProcess
# Create your forms here.
class ConfigureNewProcessForm(forms.ModelForm):
    class Meta:
        model = ConfigureNewProcess
        fields = '__all__'