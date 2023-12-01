from django.urls import path
from .roomsViews import CreateRoom, ListRooms, GetRoom, UpdateRoom, DeleteRoom
from .reservationViews import create_reservation,list_reservations,get_reservation,update_reservation,delete_reservation

urlpatterns = [
    path("create",  CreateRoom.as_view(), name="create_room"),
    path(" ", ListRooms.as_view() ,name="list_rooms"),
    path("<int:room_id>", GetRoom.as_view(), name="get_room"),
    path("<int:room_id>/update", UpdateRoom.as_view(), name="update_room"),
    path("<int:room_id>/delete", DeleteRoom.as_view(), name="delete_room"),

    path("reservation/create", create_reservation, name="create_reservation"),
    path("reservation/", list_reservations, name="list_reservations"),
    path("reservation/<int:reservation_id>", get_reservation, name="get_reservation"),
    path("reservation/<int:reservation_id>/update", update_reservation, name="update_reservation"),
    path("reservation/<int:reservation_id>/delete", delete_reservation, name="delete_reservation"),
] 
