from django.urls import path
from .views import create_user, list_users, get_user, update_user, delete_user, LoginUser

urlpatterns = [
    # path('login', login_user, name='login_user'),
    path('create', create_user.as_view(), name='create_user'),

    # /api/users/get
    path('get', list_users.as_view(), name='list_users'),

    # /api/users/get/<int:user_id>
    path('get/<int:user_id>', get_user.as_view(), name='get_user'),

    # /api/users/<int:user_id>/update
    path('<int:user_id>/update', update_user.as_view(), name='update_user'),

    # /api/users/<int:user_id>/delete
    path('<int:user_id>/delete', delete_user.as_view(), name='delete_user'),

    # /api/users/login
    path('login', LoginUser.as_view(), name='login_user'),
    
    
]
