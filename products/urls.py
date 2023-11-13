from django.urls import path
from .views import create_product, list_products, get_product, update_product, delete_product

urlpatterns = [
    path('create', create_product, name='create_product'),
    path('', list_products, name='list_products'),
    path('<int:product_id>', get_product, name='get_product'),
    path('<int:product_id>/update', update_product, name='update_product'),
    path('<int:product_id>/delete', delete_product, name='delete_product'),
]
