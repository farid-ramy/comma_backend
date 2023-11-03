from django.urls import path
from . import views

urlpatterns = [
    path('users/add', views.addUser),
    path('userss', views.getAllUsers),
    path('users/update/<int:userId>', views.updateUser),
    path('users/delete/<int:userId>', views.deleteUser),
    path('users/handel_login', views.handleLogin),
    path('users/<int:userId>', views.getUserById),
]