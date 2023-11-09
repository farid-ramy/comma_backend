from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import HistorySerializer
from .models import History
from django.utils import timezone 

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
def filterHistory(request):
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

    serializer = HistorySerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(["DELETE"])
def deleteHistory(request, historyId):
    try:
        history = History.objects.get(pk=historyId)
        history.delete()
        return Response({'message': 'History deleted successfully'})
    except History.DoesNotExist:
        return Response({'error': 'History not found'})

@csrf_exempt
@api_view(["POST"])
def checkIn(request):
    serializer = HistorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(["PUT"])
def checkOut(request, historyId):
    try:
        history_instance = History.objects.get(pk=historyId)
    except History.DoesNotExist:
        return Response({'error': 'History not found'})

    payment = request.data.get('payment')

    if payment is not None:
        history_instance.check_out_time = timezone.now()
        history_instance.payment = payment
        history_instance.save()

        serializer = HistorySerializer(history_instance)
        return Response(serializer.data)
    else:
        return Response({'error': 'Payment is required'})
