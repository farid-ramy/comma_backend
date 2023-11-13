from django.urls import path
from . import views


urlpatterns = [
    path("add/<int:branchId>", views.create_product),
    path("get/<int:branchId>/<int:productId>",views.get_product),
    path("getallproducts/<int:branchId>",views.list_products),
    path ("update/<int:productId>/<int:branchId>",views.update_product)
]