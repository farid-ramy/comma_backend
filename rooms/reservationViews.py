from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Reservation
from .serializers import ReservationSerializer ,CreateReservationSerializer

# /api/reservations/create
@api_view(['POST'])
def create_reservation(request):
    serializer = CreateReservationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    
# /api/reservations/get
@api_view(['GET'])
def list_reservations(request):
    query_params = request.query_params
    query = {}
    for key, value in query_params.items():
        if not key or not value:
            return Response({"error": "Invalid query parameter provided."})
        query[key] = value

    try:
        reservations = Reservation.objects.filter(**query)
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)})

# /api/reservations/get/<int:reservation_id>
@api_view(['GET'])
def get_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    serializer = ReservationSerializer(reservation)
    return Response(serializer.data)

# /api/reservations/<int:reservation_id>/update
@api_view(['PUT'])
def update_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    serializer = CreateReservationSerializer(reservation, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

# /api/reservations/<int:reservation_id>/delete
@api_view(['DELETE'])
def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    reservation.delete()
    return Response({'message': 'reservation deleted successfully'})
