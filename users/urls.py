from django.urls import path
from . import views

urlpatterns = [
    path('test/<int:test>', views.test),
    path('add', views.addUser),
    path('get_users', views.getAllUsers),
    path('get_users/clients', views.getAllClients),
    path('get_users/admins', views.getAllAdmins),
    path('get_users/managers', views.getAllManagers),
    path('update/<int:userId>', views.updateUser),
    path('delete/<int:userId>', views.deleteUser),
    path('handel_login', views.handleLogin),
    path('get_users/<int:userId>', views.getUserById),
]