from django import forms
from apply.models import Application

class UserApplication(forms.ModelForm):
    
    class Meta():
        model = Application
        fields = "__all__"