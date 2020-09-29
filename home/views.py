from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import User
import json 
from django.contrib.auth.decorators import login_required

@login_required
def instructions(request):
    return render(request, 'home/instructions.html')

def thankyou(request):
    return render(request, 'home/ThankYou.html')

def generate_user(request):
    with open('data.json', encoding="utf8") as file: 
        data = json.load(file) 
        
        for u in data['RECORDS']:
            if not User.objects.filter(email=u['email']):
                user =  User(name=u['name'], email=u['email'], password="edcrecruitments")
                user.save()
    return redirect('thank-you')

def destroy_user(request):
    users = User.objects.exclude(start_time=NULL)
    if users:
        for user in users:
            user.password = "UIkV1Jyk4V5p6dDOfOZx"
        user.save()
    return redirect('thank-you')