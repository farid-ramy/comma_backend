from django.urls import path
from .views import create_user, list_users, get_user, update_user, delete_user, login_user

urlpatterns = [
    path('create/', create_user.as_view(), name='create_user'),
    path('get/', list_users.as_view(), name='list_users'),
    path('get/<int:user_id>/', get_user.as_view(), name='get_user'),
    path('<int:user_id>/update/', update_user.as_view(), name='update_user'),
    path('<int:user_id>/delete/', delete_user.as_view(), name='delete_user'),

    path('login/', login_user.as_view(), name='login_user'), 
]
