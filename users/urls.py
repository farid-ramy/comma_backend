from django.urls import path
from . import views

urlpatterns = [
    path('add', views.addUser),
    path('get_users', views.getAllUsers),
    path('get_users/employees', views.getAllEmployees),
    path('get_users/clients', views.getAllClients),
    path('update/<int:userId>', views.updateUser),
    path('delete/<int:userId>', views.deleteUser),
    path('handel_login', views.handleLogin),
    path('get_users/<int:userId>', views.getUserById),
]