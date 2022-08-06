from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.


def login_page(request):
    return render(request, 'accounts/login.html')

def register_page(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        
        user_obj = User.objects.filter(username=email)
        if user_obj.exists():
            messages.warning(request, 'Email already exists')
            return HttpResponseRedirect(request.path_info)
        
        user = User.objects.create(email= email,username=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()

    return render(request, 'accounts/register.html')