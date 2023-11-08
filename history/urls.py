from django.urls import path
from . import views

urlpatterns = [
    path("" , views.getHistory),
    path('filter', views.filterHistory),
    path('delete/<int:historyId>', views.deleteHistory),
    path('check_in', views.checkIn),
    path('check_out/<int:historyId>', views.checkOut),
]
