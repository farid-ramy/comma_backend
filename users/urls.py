from django.urls import path
from .views import create_user, user_list, get_user, update_user, delete_user, user_login

urlpatterns = [
    path('', user_list, name='user_list'),
    path('<int:pk>', get_user, name='get_user'),
    path('create', create_user, name='create_user'),
    path('<int:pk>/update', update_user, name='update_user'),
    path('<int:pk>/delete', delete_user, name='delete_user'),

    path('login', user_login, name='user_login'),
]
