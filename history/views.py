from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import HistorySerializer, CreateHistorySerializer
from .models import History
from users.models import User
from branches.models import Branch

# /api/history/create
@api_view(["POST"])
def history_create(request):
    client = request.data.get('client')
    employee = request.data.get('employee')
    branch = request.data.get('branch')

    if not client or not User.objects.filter(pk=client).exists():
        return Response({"error": "Invalid or missing client"})

    if not employee or not User.objects.filter(pk=employee).exists():
        return Response({"error": "Invalid or missing employee"})

    if not branch or not Branch.objects.filter(pk=branch).exists():
        return Response({"error": "Invalid or missing branch"})

    serializer = CreateHistorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

# /api/history
@api_view(["GET"])
def list_histories(request):
    query_params = request.query_params
    query = Q()

    for key, value in query_params.items():
        if not key:
            return Response({"error": "Invalid query parameter provided."})

        if value == "None" or value == 'null':
            value = "None"
            query &= Q(**{f"{key}__isnull": True})
        else:
            query &= Q(**{key: value})

    try:
        histories = History.objects.filter(query)
        serializer = HistorySerializer(histories, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)})

# /api/history/<int:history_id>
@api_view(["GET"])
def get_history(request, history_id):
    history = get_object_or_404(History, id=history_id)
    serializer = HistorySerializer(history)
    return JsonResponse(serializer.data)

# /api/history/<int:history_id>/update
@api_view(['PUT'])
def update_history(request, history_id):
    history = get_object_or_404(History, id=history_id)
    serializer = CreateHistorySerializer(history, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    
# /api/history/<int:history_id>/delete
@api_view(["DELETE"])
def delete_history(request, history_id):
    try:
        history = History.objects.get(pk=history_id)
        history.delete()
        return Response({'message': 'History deleted successfully'})
    except History.DoesNotExist:
        return Response({'error': 'History not found'})

