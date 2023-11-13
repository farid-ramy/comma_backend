from django.urls import path
from .views import history_create, list_histories, delete_history, get_history, update_history

urlpatterns = [
    path('create', history_create, name='history_create'),
    path('', list_histories, name='list_histories'),
    path('<int:history_id>', get_history, name='get_history'),
    path('<int:history_id>/update', update_history, name="update_history"),
    path('<int:history_id>/delete', delete_history, name="delete_history"),
]
