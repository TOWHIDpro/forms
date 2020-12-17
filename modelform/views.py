from django.shortcuts import render
#form .models import modelform

# Create your views here.

def modelform(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        username   = request.POST['username']
        email      = request.POST['email']
        password1  = request.POST['password1']
        password2  = request.POST['password2']
        


    return render(request, "modelform.html")