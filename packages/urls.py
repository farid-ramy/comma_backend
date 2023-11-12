from django.urls import path
from .views import create_package, list_packages, get_package, update_package, delete_package

urlpatterns = [
    path("create", create_package, name='create_package'),
    path("", list_packages, name="list_packages"),
    path("<int:package_id>", get_package, name="get_package"),
    path("<int:package_id>/update", update_package, name="update_package"),
    path("<int:package_id>/delete", delete_package, name="delete_package"),
]
