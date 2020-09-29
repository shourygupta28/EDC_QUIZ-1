from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
# Create your views here.
# def user_login(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request=request, data=request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(email = email, password = password)
#             if user is not None:
#                 login(request, user)
#                 return render(request, 'questions/index.html')
#             else:
#                 messages.success(request, f'Wrong email id or password')
#                 form = AuthenticationForm()
#     context = {
#         'form':form
#     }
#     return render(request, 'home/login.html', context)

def instructions(request):
    return render(request, 'home/instructions.html')

def thankyou(request):
    return render(request, 'home/ThankYou.html')