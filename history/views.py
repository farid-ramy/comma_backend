from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import HistorySerializer
from .models import History
from django.utils import timezone 
from django.http import JsonResponse

# /api/history
def getHistory(request):
    histories = History.objects.all()
    serialized_histories = []
    for history in histories:
        serialized_history = {
            "client_id": history.client_id.id,
            "client_role": history.client_id.role,
            "client_first_name": history.client_id.first_name,
            "client_last_name": history.client_id.last_name,
            "client_username": history.client_id.username,
            "client_password": history.client_id.password,
            "client_phone": history.client_id.phone,
            "client_email": history.client_id.email,
            "client_national_id": history.client_id.national_id,
            "client_age": history.client_id.age,
            "client_job": history.client_id.job,
            "client_address": history.client_id.address,
            "client_created_at": history.client_id.created_at.isoformat(),
            "client_modified_at": history.client_id.modified_at.isoformat(),
            "id": history.id,
            "checkin_time": history.checkin_time.isoformat(),
            "checkout_time": history.checkout_time.isoformat() if history.checkout_time else None,
            "price": float(history.price) if history.price else None,
            "employee_id": history.employee_id.id,
            "branch_id": history.branch_id.id
        }
        serialized_histories.append(serialized_history)

    # Return the serialized data as JSON response
    return JsonResponse(serialized_histories, safe=False)


# /api/history?...
@api_view(["GET"])
def filterHistory(request):
    queryset = History.objects.all()

    checkin_time = request.query_params.get('checkin_time')
    if checkin_time:
        queryset = queryset.filter(checkin_time__date=checkin_time)

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


# /api/history/delete<int:historyId>
@api_view(["DELETE"])
def deleteHistory(request,historyId):
    try:
        history = History.objects.get(pk=historyId)
        history.delete()
        return Response({'message': 'History deleted successfully'})
    except:
        return Response({'error': 'History not found'})


# /api/history/check_in
@csrf_exempt 
@api_view(["POST"])
def checkIn(request): 
    serializer = HistorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


# /api/history/check_out/<int:historyId>
@api_view(["PUT"])
def checkOut(request,historyId):    
    try:
        history_instance = History.objects.get(pk=historyId)
    except:
        return Response({'error': 'History not found'})

    price = request.data.get('price')

    if price is not None:
        history_instance.checkout_time = timezone.now()
        history_instance.price = price
        history_instance.save()

        serializer = HistorySerializer(history_instance)
        return Response(serializer.data)
    else:
        return Response({'error': 'Price is requires'})
