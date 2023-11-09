from django.urls import path
from .views import getAllProducts, getProductById, addProduct, updateProduct, deleteProduct

urlpatterns = [
    path('getproducts', getAllProducts, name='get_all_products'),
    path('getproduct/<int:productId>', getProductById, name='get_product_by_id'),
    path('add', addProduct, name='add_product'),
    path('update/<int:productId>', updateProduct, name='update_product'),
    path('delete/<int:productId>', deleteProduct, name='delete_product'),
]
