from django import forms
from .models import EmployeeModel

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=EmployeeModel
        fields='__all__'
        # fields=['fieldname1','fieldname2',.....'fieldNamen]
        #fields=['name']
        exclude=['age']

