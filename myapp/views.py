from django.shortcuts import render
from .forms import EmployeeForm

# Create your views here.

def home(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    form=EmployeeForm()
    return render(request,'home.html',context={'form':form})

