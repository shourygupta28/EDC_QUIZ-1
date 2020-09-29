from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
]

