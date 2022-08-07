from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from .models import Profile

# Create your views here.

'''
Login page
'''
def login_page(request):
    if request.method == 'POST':
        
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=email)
        
        if not user_obj.exists():
            messages.warning(request, 'Account not found ')
            return HttpResponseRedirect(request.path_info)
        
        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, 'Please verify your email')
            return HttpResponseRedirect(request.path_info)
        
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            return redirect('/')
        
        
        messages.warning(request, 'Invalid credentials')
        return HttpResponseRedirect(request.path_info)
    
    return render(request, 'accounts/login.html')


'''
Register page
'''
def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # print(request.POST)
        user_obj = User.objects.filter(username=email)
        
        if user_obj.exists():
            messages.warning(request, 'Email already exists')
            print('Email already exists')
            return HttpResponseRedirect(request.path_info)
        
        user = User.objects.create(email= email,username=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        
        messages.success(request, 'An email has been sent on your mail')
        return HttpResponseRedirect(request.path_info)

    return render(request, 'accounts/register.html')

'''
Activate Email
'''
def activate_email(request, email_token):
    try:
        user = Profile.objects.get(email_token=email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Invalid Email Token')