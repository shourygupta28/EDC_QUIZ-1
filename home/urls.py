from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home import views
from .views import instructions, thankyou, generate_user, destroy_user
from questions import views as ques_view

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='home/login.html')),
    path('instructions/', instructions, name='instructions'),
    path('thank-you/', thankyou, name='thank-you'),
    path('questions/', ques_view.question, name='questions'),
    path('LueZJNIQvZzW78EneDeX/', generate_user, name='generate-user'),
    path('lWwK7LIEGXS108i6sRSi/', destroy_user, name='generate-user'),
]