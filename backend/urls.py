from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('api/', include("users.urls")),
    path('api/packages/', include('packages.urls')),
    path('api/branches/',include ("branches.urls")),
    path('admin/', admin.site.urls),
]
