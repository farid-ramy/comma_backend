from django.urls import path
from .views import history_list ,history_detail,filterHistory,deleteHistory,checkIn,checkOut

urlpatterns = [
    path('', history_list, name='history_list'),
    path('<int:history_id>', history_detail, name='history_detail'),
    path('filter', filterHistory),
    path('delete/<int:historyId>', deleteHistory),
    path('check_in', checkIn),
    path('check_out/<int:historyId>', checkOut),
]
