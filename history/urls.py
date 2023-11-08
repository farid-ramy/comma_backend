from django.urls import path
from . import views

urlpatterns = [
    path("" , views.getHistory),
    path('checkin/<int:user_id>/<int:branch_id>', views.checkIn),
    path('checkout/<int:user_id>/<int:branch_id>', views.checkOut),
]
