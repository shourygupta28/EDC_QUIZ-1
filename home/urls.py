from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home import views
from .views import instructions, thankyou
from questions import views as ques_view

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='home/login.html')),
    path('instructions/', views.instructions, name='instructions'),
    path('thank-you/', views.thankyou, name='thank-you'),
    path('questions/', ques_view.question, name='questions')
]