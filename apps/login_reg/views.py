from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime, date, time
from .models import User
##########################HOMEPAGE###################


def index(request):
    return render(request, 'login_reg/index.html')
#####################USERS PAGE GET###################


def show_users(request):
    context = {
        "show_users": User.objects.all()
    }
    return render(request, "login_reg/show_users.html", context)


def reg(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        if request.method == 'POST':
            register = User.objects.create(
            first_name=request.POST['first_name'], 
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=request.POST['password'])
        request.session['first_name'] = request.POST['first_name']
    return redirect('/wall')

########################################## LOGOUT ##########################################

def login(request):
    
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)
        if not errors['status']:
            for key, value in errors['errors'].items():
                messages.error(request ,value,)
            return redirect('/')
        else: 
            this_user = User.objects.get(email = request.POST['loginEmail'])
            request.session['first_name'] = this_user.first_name
            request.session['id'] = this_user.id
        messages.success(request, 'Login Successful')
        return redirect('/wall')

########################################## LOGOUT ##########################################

def logout(request):
    request.session.clear()
    return redirect('/')




