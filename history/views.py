from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import HistorySerializer
from .models import History
from users.models import User
from branches.models import Branch

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
        instance = History(
            client_id = User.objects.get(pk=request.data.get('client_id')),
            employee_id = User.objects.get(pk=request.data.get('employee_id')),
            branch_id = Branch.objects.get(pk=request.data.get('branch_id')),
        )
        
        instance.save()
        return Response({"message": "Instance added successfully"})
    except User.DoesNotExist:
        return Response({"error": "User does not exist"})
    except Branch.DoesNotExist:
        return Response({"error": "Branch does not exist"})
    except Exception as e:
        return Response({"error": str(e)})






