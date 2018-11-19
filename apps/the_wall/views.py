from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime, date, time
from .models import Message, Comment
from apps.login_reg.models import User
##########################HOMEPAGE###################


def index(request):

    context={
            'comments' : Comment.objects.all(),
            'messages' : Message.objects.all(),
            'users' : User.objects.all(),
            }
    return render(request, 'the_wall/index.html', context)

def postMSG(request):
    if request.method == 'POST':
            Message.objects.create(
            message=request.POST['commentBox1'],
            user=User.objects.get(id=request.session['id']))
    return redirect ('/wall')

def postCMT(request):
    if request.method =='POST':
            Comment.objects.create(
            user=User.objects.get(id=request.session['id']), 
            comment=request.POST['commentBox2'])
    return redirect('/wall')
