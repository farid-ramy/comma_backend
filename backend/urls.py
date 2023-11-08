from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('api/users/', include("users.urls")),
    path('api/packages/', include('packages.urls')),
    path('api/branches/',include ("branches.urls")),
    path('api/kitchen/',include ("kitchen.urls")),
    path('api/history/',include ("history.urls")),
    path('admin/', admin.site.urls),

]
