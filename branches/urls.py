from django.urls import path
from . import views


urlpatterns = [
    path('branches/addBranch', views.addBranch),
    path ('branches/<int:branchId>/', views.getBranchById),
    path ('branches/delete/<int:branchId>', views.deleteBranch),
   path ('branches/update/<int:branchId>', views.updateBranch),
    path('branches', views.getAllBranches)
]