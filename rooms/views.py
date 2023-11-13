from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Room
from .serializers import RoomSerializer
from .models import Branch



@api_view(['POST'])
def create_room(request, branch_id):
    try:
        branch = Branch.objects.get(pk=branch_id)
        room = Room(branch=branch, **request.data)
        serializer = RoomSerializer(instance=room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Branch.DoesNotExist:
        return Response({'error': 'Branch not found'}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(["GET"])
def list_rooms(request, branch_id):
    query_params = request.query_params
    query = {"branch_id": branch_id}

    for key, value in query_params.items():
        if not key or not value:
            return Response({"error": "Invalid query parameter provided."})
        query[key] = value

    try:
        rooms_in_branch = Room.objects.filter(**query)
        if rooms_in_branch.exists():
            serializer = RoomSerializer(rooms_in_branch, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'No rooms found in the branch'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)})

@api_view(['GET'])
def get_room(request, branch_id, room_id):
    try:
        room = Room.objects.get(branch_id=branch_id, pk=room_id)
        serializer = RoomSerializer(room)
        return Response(serializer.data)
    except Room.DoesNotExist:
        return Response({'error': 'Room not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_room(request, branch_id, room_id):
    try:
        room = Room.objects.get(branch_id=branch_id, pk=room_id)
        serializer = RoomSerializer(room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Room.DoesNotExist:
        return Response({'error': 'Room not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_room(request, branch_id, room_id):
    try:
        room = Room.objects.get(branch_id=branch_id, pk=room_id)
        room.delete()
        return Response({'message': 'Room deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Room.DoesNotExist:
        return Response({'error': 'Room not found'}, status=status.HTTP_404_NOT_FOUND)


