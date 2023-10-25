from django.urls import path
from . import views

urlpatterns = [
  
    path('branches/<int:branch_id>/add-kitchen/', views.addKitchenForBranch, name='add-kitchen-for-branch'),
    path('branches/<int:branch_id>/kitchen/<int:kitchen_id>/', views.getBranchWithKitchen, name='get_branch_with_kitchen'),
    path('branches/<int:branch_id>/kitchen/<int:kitchen_id>/add-product/', views.addProductToKitchen, name='add_product_to_kitchen')

]
