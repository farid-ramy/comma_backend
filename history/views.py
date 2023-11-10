from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import HistorySerializer
from .models import History
from users.models import User
from branches.models import Branch
from django.db.models import Q

@api_view(["GET"])
def history_list(request):
    histories = History.objects.all()
    serializer = HistorySerializer(histories, many=True)
    return JsonResponse(serializer.data , safe=False)

@csrf_exempt
@api_view(["GET"])
def history_detail(request, history_id):
    history = get_object_or_404(History, id=history_id)
    serializer = HistorySerializer(history)
    return JsonResponse(serializer.data)

@api_view(["GET"])
def filter_history(request):
    queryset = History.objects.all()

    check_in_time = request.query_params.get('check_in_time')
    if check_in_time:
        queryset = queryset.filter(check_in_time__date=check_in_time)

    branch_id = request.query_params.get('branch_id')
    if branch_id:
        queryset = queryset.filter(branch_id=branch_id)

    employee_id = request.query_params.get('employee_id')
    if employee_id:
        queryset = queryset.filter(employee_id=employee_id)

    client_id = request.query_params.get('client_id')
    if client_id:
        queryset = queryset.filter(client_id=client_id)

    check_out_time = request.query_params.get('check_out_time')
    if check_out_time:
        queryset = queryset.exclude(Q(check_out_time__isnull=False))

    serializer = HistorySerializer(queryset, many=True)
    return Response(serializer.data)

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
        client_id = request.data.get('client_id')
        employee_id = request.data.get('employee_id')
        branch_id = request.data.get('branch_id')

        if not client_id or not User.objects.filter(pk=client_id).exists():
            return Response({"error": "Invalid or missing client_id"})

        if not employee_id or not User.objects.filter(pk=employee_id).exists():
            return Response({"error": "Invalid or missing employee_id"})

        if not branch_id or not Branch.objects.filter(pk=branch_id).exists():
            return Response({"error": "Invalid or missing branch_id"})

        instance = History(
            client_id=User.objects.get(pk=client_id),
            employee_id=User.objects.get(pk=employee_id),
            branch_id=Branch.objects.get(pk=branch_id),
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


