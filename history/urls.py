from django.urls import path
from .views import history_create, list_histories

urlpatterns = [
    path('create', history_create, name='history_create'),
    path('', list_histories, name='list_histories'),

    # path('<int:history_id>', history_detail, name='history_detail'),
    # path('filter', filter_history, name="filter_history"),
    # path('<int:history_id>/delete', delete_history, name="delete_history"),
    # path('check_in', check_in, name="check_in"),
    # path('<int:history_id>/check_out', check_out, name="check_out"),
]
