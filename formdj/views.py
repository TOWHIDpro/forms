from django.shortcuts import render
from .forms import customersform

# Create your views here.
def djform(request):
    form = customersform()
    if request.method == 'POST':
        form = customersform(request.POST)
        if form.is_valid():
            form.save()


    return render(request, "djform.html", {
        'form':form
    })