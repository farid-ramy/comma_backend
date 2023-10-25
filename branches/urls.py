from django.urls import path
from . import views

urlpatterns = [
    path ('', views.getAllBranches),
    path ('add', views.addBranch),
    path ('<int:branchId>/', views.getBranchById),
    path ('delete/<int:branchId>', views.deleteBranch),
    path ('update/<int:branchId>', views.updateBranch),
]