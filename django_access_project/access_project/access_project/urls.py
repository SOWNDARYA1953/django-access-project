from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('home/', views.home, name='home'),
]