from django.urls import path
from .views import CreatePackage, ListPackages, GetPackage, UpdatePackage, DeletePackage

urlpatterns = [
    path('create', CreatePackage.as_view(), name='create_package'),
    path('', ListPackages.as_view(), name='list_packages'),
    path('<int:package_id>', GetPackage.as_view(), name='get_package'),
    path('<int:package_id>/update', UpdatePackage.as_view(), name='update_package'),
    path('<int:package_id>/delete', DeletePackage.as_view(), name='delete_package'),
]
