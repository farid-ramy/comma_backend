from django.urls import path
from . import views


urlpatterns = [
    path("add/<int:branchId>", views.addProductToBranch),
    path("get/<int:branchId>/<int:productId>",views.getProductById),
    path("getallproducts/<int:branchId>",views.getAllProductsInBranch),
    path ("update/<int:productId>/<int:branchId>",views.updateproduct)
]