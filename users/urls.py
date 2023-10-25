from django.urls import path
from . import views

urlpatterns = [
    path('userss', views.getAllUsers),
    path('users/add', views.addUser),
    path('users/update/<int:userId>', views.updateUser),
    path('users/delete/<int:userId>', views.deleteUser),
    path('users/<int:userId>', views.getUserById),
    path('handel_login', views.handleLogin),
]