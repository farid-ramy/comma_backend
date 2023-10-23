from django.urls import path
from . import views

urlpatterns = [
    path('users/add', views.addUser),
    path('users', views.getAllUsers),
    path('users/<int:userId>', views.getUserById),
    path('users/update/<int:userId>', views.updateUser),
    path('users/delete/<int:userId>', views.deleteUser),
    path('handel_login', views.handelLogin),
]