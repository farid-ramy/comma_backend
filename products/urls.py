from django.urls import path
from .views import CreateProduct, ListProducts, GetProduct, UpdateProduct, DeleteProduct

urlpatterns = [
    path('create', CreateProduct.as_view(), name='create_product'),
    path('', ListProducts.as_view(), name='list_products'),
    path('<int:product_id>', GetProduct.as_view(), name='get_product'),
    path('<int:product_id>/update', UpdateProduct.as_view(), name='update_product'),
    path('<int:product_id>/delete', DeleteProduct.as_view(), name='delete_product'),
]
