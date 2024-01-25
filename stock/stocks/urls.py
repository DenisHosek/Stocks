from django.urls import path
from django.contrib.auth import views as vie

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("logout/", vie.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('account/', vie.PasswordChangeView.as_view(template_name='account.html'), name='account'),
    path('account/pass/', views.change_pass, name='password_change_done'),
    path("register/", views.singup, name="register"),
    path("login/", vie.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('stock/add/', views.add_stock, name="add_stock"),
    ]
