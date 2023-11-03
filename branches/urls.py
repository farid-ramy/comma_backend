from django.urls import path
from . import views

urlpatterns = [
    path('add', views.addBranch),
    path('', views.getAllBranches),
    path('update/<int:branchId>', views.updateBranch),
    path('delete/<int:branchId>', views.deleteBranch),
    path('<int:branchId>', views.getBranchById),
]