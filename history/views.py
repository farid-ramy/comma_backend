from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import HistorySerializer
from .models import History
from django.utils import timezone 

# /api/history
@api_view(["GET"])
def getHistory(request):
    history_data = History.objects.all()  
    serializer = HistorySerializer(history_data, many=True)
    return Response(serializer.data)

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
