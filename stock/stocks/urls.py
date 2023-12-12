from django.urls import path
from django.contrib.auth import views as vie

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("logout/", vie.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('account/', vie.PasswordChangeView.as_view(template_name='account.html'), name='account'),
    path('stock/', views.stock, name='stock'),
    path("register/", views.singup, name="register"),
    path("login/", vie.LoginView.as_view(template_name='registration/login.html'), name='login'),
]
