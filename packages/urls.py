from django.urls import path
from . import views

urlpatterns = [
    path("add", views.addPackage),
    path("", views.getAllPackages),
    path("update/<int:packageId>", views.updatePackage),
    path("<int:packageId>/", views.getPackageById),
    path("delete/<int:packageId>", views.deletePackage),
    path("offer/<int:packageId>",views.offeroption)
]
