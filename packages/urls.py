from django.urls import path
from . import views

urlpatterns = [
    path("packages", views.getAllPackages),
    path("packages/add", views.addPackage),
    path("packages/<int:packageId>/", views.getPackageById),
    path("packages/update/<int:packageId>", views.updatePackage),
    path("packages/delete/<int:packageId>", views.deletePackage),
]
