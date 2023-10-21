from django.urls import path
from . import views

urlpatterns = [
    path('packages/add/', views.add_package, name='add_package'),
    
    path('packages/', views.get_all_packages, name='get_all_packages'),
    path('packages/<int:package_id>/', views.get_package_by_id, name='get_package_by_id'),
   
    path('packages/update/<int:package_id>/', views.update_package, name='update_package'),
    path('packages/delete/<int:package_id>/', views.delete_package, name='delete_package'),

]