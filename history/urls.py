from django.urls import path
from . import views

urlpatterns = [

    path('checkin/<int:user_id>/<int:branch_id>/', views.check_in, name='checkin'),
    path('checkout/<int:user_id>/<int:branch_id>/', views.check_out),
]
