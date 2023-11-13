from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import HistorySerializer, CreateHistorySerializer
from .models import History
from users.models import User
from branches.models import Branch
from django.db.models import Q

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

@api_view(["GET"])
def list_histories(request):
    query_params = request.query_params
    query = {}
    for key, value in query_params.items():
        if not key or not value:
            return Response({"error": "Invalid query parameter provided."})
        query[key] = value

    try:
        histories = History.objects.filter(**query)
        serializer = HistorySerializer(histories, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)})
    





























@api_view(["GET"])
def history_detail(request, history_id):
    history = get_object_or_404(History, id=history_id)
    serializer = HistorySerializer(history)
    return JsonResponse(serializer.data)

@api_view(["GET"])
def filter_history(request):
    pass
    # queryset = History.objects.all()

    # check_in_time = request.query_params.get('check_in_time')
    # if check_in_time:
    #     queryset = queryset.filter(check_in_time__date=check_in_time)

    # branch = request.query_params.get('branch')
    # if branch:
    #     queryset = queryset.filter(branch=branch)

    # employee = request.query_params.get('employee')
    # if employee:
    #     queryset = queryset.filter(employee=employee)

    # client = request.query_params.get('client')
    # if client:
    #     queryset = queryset.filter(client=client)

    # check_out_time = request.query_params.get('check_out_time')
    # if check_out_time:
    #     queryset = queryset.exclude(Q(check_out_time__isnull=False))

    # serializer = HistorySerializer(queryset, many=True)
    # return Response(serializer.data)

@api_view(["DELETE"])
def delete_history(request, history_id):
    try:
        history = History.objects.get(pk=history_id)
        history.delete()
        return Response({'message': 'History deleted successfully'})
    except History.DoesNotExist:
        return Response({'error': 'History not found'})

@api_view(["POST"])
def check_in(request):
    try:
        client = request.data.get('client')
        employee = request.data.get('employee')
        branch = request.data.get('branch')

        if not client or not User.objects.filter(pk=client).exists():
            return Response({"error": "Invalid or missing client"})

        if not employee or not User.objects.filter(pk=employee).exists():
            return Response({"error": "Invalid or missing employee"})

        if not branch or not Branch.objects.filter(pk=branch).exists():
            return Response({"error": "Invalid or missing branch"})

        instance = History(
            client=User.objects.get(pk=client),
            employee=User.objects.get(pk=employee),
            branch=Branch.objects.get(pk=branch),
        )

        instance.save()
        return Response({"message": "Instance added successfully"})
    except Exception as e:
        return Response({"error": str(e)})

@api_view(["PUT"])
def check_out(request, history_id):
    history = get_object_or_404(History, pk=history_id)
    if history.check_out_time is not None:
        return JsonResponse({'error': 'History not found'})
    history.check_out_time = timezone.now()
    history.payment = request.data.get("payment")
    history.save()
    return JsonResponse({'message': 'Check-out successful'})


