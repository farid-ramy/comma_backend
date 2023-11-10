from django.urls import path
from .views import history_list, history_detail, filter_history, delete_history, check_in, check_out

urlpatterns = [
    path('', history_list, name='history_list'),
    path('<int:history_id>', history_detail, name='history_detail'),
    path('filter', filter_history, name="filter_history"),
    path('<int:history_id>/delete', delete_history, name="delete_history"),
    path('check_in', check_in, name="check_in"),
    path('check_out', check_out, name="check_out"),


]
