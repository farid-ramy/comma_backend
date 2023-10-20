from django.urls import path
from . import views

urlpatterns = [
    path('add_user', views.add_user,name='add_user'),
    path('get_all_users', views.get_all_users, name='get_all_users'),
    path('get_user_by_id/<int:user_id>', views.get_user_by_id, name='get_user_by_id'),
    path('update_user/<int:user_id>', views.update_user, name='update_user'),
    path('delete_user/<int:user_id>', views.delete_user,name='delete_user'),
    path('handel_login', views.handel_login,name='handel_login'),
]