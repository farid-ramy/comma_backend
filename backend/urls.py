from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('api/', include("users.urls")),
    path('api/', include('packages.urls')),
    path ('api/',include ("branches.urls"))
        path ('api/',include ("kitchen.urls")),
    path('admin/', admin.site.urls),
]
