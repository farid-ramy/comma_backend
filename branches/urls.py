from django.urls import path
from . import views


urlpatterns = [
    path('branches/addBranch', views.addBranch),

]