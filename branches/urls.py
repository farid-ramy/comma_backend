from django.urls import path
from . import views

urlpatterns = [
    path('branches/add', views.addBranch),
    path ('branches/<int:branchId>/', views.getBranchById),
    path ('branches/delete/<int:branchId>', views.deleteBranch)
]