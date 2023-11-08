from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD

    path('checkin/<int:user_id>/<int:branch_id>/', views.check_in, name='checkin'),
    path('checkout/<int:user_id>/<int:branch_id>/', views.check_out),
=======
    path("" , views.getHistory),
    path('filter', views.filterHistory),
    path('delete/<int:historyId>', views.deleteHistory),
    path('check_in', views.checkIn),
    path('check_out/<int:historyId>', views.checkOut),
>>>>>>> f8752a7950c5100d3975743722e10dbde455a2e1
]
