from django.urls import path
from .views import create_user, list_users, get_user, update_user, delete_user, login_user

urlpatterns = [
    path('create', create_user, name='create_user'),
    path('get', list_users, name='list_users'),
    path('get/<int:user_id>', get_user, name='get_user'),
    path('<int:user_id>/update', update_user, name='update_user'),
    path('<int:user_id>/delete', delete_user, name='delete_user'),

    path('login', login_user, name='login_user'),
]
