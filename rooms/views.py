from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Room
from .serializers import RoomSerializer ,CreateRoomSerializer

# /api/rooms/create
@api_view(['POST'])
def create_room(request):
    serializer = CreateRoomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    
# /api/rooms/get
@api_view(['GET'])
def list_rooms(request):
    query_params = request.query_params
    query = {}
    for key, value in query_params.items():
        if not key or not value:
            return Response({"error": "Invalid query parameter provided."})
        query[key] = value

    try:
        rooms = Room.objects.filter(**query)
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)})

# /api/rooms/get/<int:room_id>
@api_view(['GET'])
def get_room(request, room_id):
    room = get_object_or_404(room, id=room_id)
    serializer = RoomSerializer(room)
    return Response(serializer.data)

# /api/rooms/<int:room_id>/update
@api_view(['PUT'])
def update_room(request, room_id):
    room = get_object_or_404(room, id=room_id)
    serializer = CreateRoomSerializer(room, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

# /api/rooms/<int:room_id>/delete
@api_view(['DELETE'])
def delete_room(request, room_id):
    room = get_object_or_404(room, id=room_id)
    room.delete()
    return Response({'message': 'room deleted successfully'})
