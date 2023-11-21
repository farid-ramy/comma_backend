from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('api/users/', include("users.urls")),
    path('api/packages/', include('packages.urls')),
    path('api/branches/',include ("branches.urls")),
    path('api/history/',include ("history.urls")),
    path('api/products/',include ("products.urls")),
    path('api/rooms/',include ("rooms.urls")),

    path('admin/', admin.site.urls),
]
