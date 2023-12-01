from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Room
from .serializers import RoomSerializer, CreateRoomSerializer

# /api/rooms/create
class CreateRoom(APIView):
    def post(self, request):
        serializer = CreateRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /api/rooms/get
class ListRooms(APIView):
    def get(self, request):
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
class GetRoom(APIView):
    def get(self, request, room_id):
        room = get_object_or_404(Room, id=room_id)
        serializer = RoomSerializer(room)
        return Response(serializer.data)

# /api/rooms/<int:room_id>/update
class UpdateRoom(APIView):
    def put(self, request, room_id):
        room = get_object_or_404(Room, id=room_id)
        serializer = CreateRoomSerializer(instance=room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# /api/rooms/<int:room_id>/delete
class DeleteRoom(APIView):
    def delete(self, request, room_id):
        room = get_object_or_404(Room, id=room_id)
        room.delete()
        return Response({'message': 'Room deleted successfully'})
