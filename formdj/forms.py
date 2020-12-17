from django import forms
from .models import customers

class customersform(forms.ModelForm):
    class Meta:
        model  = customers
        fields = ('first_name', 'last_name', 'phone', 'view')