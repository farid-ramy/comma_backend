from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAllBranches),
    path('add', views.addBranch),
    path('update/<int:branchId>', views.updateBranch),
    path('delete/<int:branchId>', views.deleteBranch),
    path('<int:branchId>', views.getBranchById),
]