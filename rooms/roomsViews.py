from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Room
from .serializers import RoomSerializer, CreateRoomSerializer

@api_view(['POST'])
class create_room(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CreateRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET'])
class list_rooms(APIView):
    def get(self, request, *args, **kwargs):
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

@api_view(['GET'])
class get_room(APIView):
    def get(self, request, room_id, *args, **kwargs):
        room = get_object_or_404(Room, id=room_id)
        serializer = RoomSerializer(room)
        return Response(serializer.data)

@api_view(['PUT'])
class update_room(APIView):
    def put(self, request, room_id, *args, **kwargs):
        room = get_object_or_404(Room, id=room_id)
        serializer = CreateRoomSerializer(room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['DELETE'])
class delete_room(APIView):
    def delete(self, request, room_id, *args, **kwargs):
        room = get_object_or_404(Room, id=room_id)
        room.delete()
        return Response({'message': 'room deleted successfully'})
