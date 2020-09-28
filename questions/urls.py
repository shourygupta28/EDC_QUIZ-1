from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import question

urlpatterns = [
    
    # path('login/', 	auth_views.LoginView.as_view(template_name='questions/login.html'),	name='login'),
    path('questions/', question, name='questions')

]

if settings.DEBUG: 
	urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT )
