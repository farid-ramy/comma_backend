from django.urls import path
from . import views

urlpatterns = [
    path("", views.getAllPackages),
    path("add", views.addPackage),
    path("<int:packageId>/", views.getPackageById),
    path("update/<int:packageId>", views.updatePackage),
    path("delete/<int:packageId>", views.deletePackage),
]
