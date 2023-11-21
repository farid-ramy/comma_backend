from django.urls import path
from .roomsViews import create_room, list_rooms, get_room, update_room, delete_room
from .reservationViews import create_reservation,list_reservations,get_reservation,update_reservation,delete_reservation

urlpatterns = [
    path("create", create_room, name="create_room"),
    path("", list_rooms, name="list_rooms"),
    path("<int:room_id>", get_room, name="get_room"),
    path("<int:room_id>/update", update_room, name="update_room"),
    path("<int:room_id>/delete", delete_room, name="delete_room"),

    path("reservation/create", create_reservation, name="create_reservation"),
    path("reservation/", list_reservations, name="list_reservations"),
    path("reservation/<int:reservation_id>", get_reservation, name="get_reservation"),
    path("reservation/<int:reservation_id>/update", update_reservation, name="update_reservation"),
    path("reservation/<int:reservation_id>/delete", delete_reservation, name="delete_reservation"),
] 
