from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:branch_id>', views.addKitchenForBranch),
    path('<int:branch_id>/kitchen/<int:kitchen_id>/', views.getBranchWithKitchen),
    path('<int:branch_id>/kitchen/<int:kitchen_id>/add-product/', views.addProductToKitchen)

]
