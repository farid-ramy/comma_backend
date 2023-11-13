from django.urls import path
from . import views


urlpatterns = [
    path("add/<int:room_id>", views.create_room),
    path("get/<int:branchId>/<int:room_id>",views.get_room),
    path("getallrooms/<int:branchId>",views.list_rooms),
    path ("update/<int:room_id>/<int:branchId>",views.update_room)
]