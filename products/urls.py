from django.urls import path
from .views import getAllProducts, getProductById, addProduct, updateProduct, deleteProduct

urlpatterns = [
    path('api/products/getproducts', getAllProducts, name='get_all_products'),
    path('api/products/getproduct/<int:productId>', getProductById, name='get_product_by_id'),
    path('api/products/add', addProduct, name='add_product'),
    path('api/products/update/<int:productId>', updateProduct, name='update_product'),
    path('api/products/delete/<int:productId>', deleteProduct, name='delete_product'),
]
