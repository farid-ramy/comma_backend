from django.urls import path
from . import views


urlpatterns = [
    path("add/<int:branchId>", views.addProductToBranch),

]