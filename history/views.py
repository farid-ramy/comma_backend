from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import History
from .serializers import HistorySerializer
from datetime import datetime
from users.models import User
from branches.models import Branch
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# View to add a new branch

@api_view(["POST"])
def calculate_price(checkin_time, checkout_time):
    if checkin_time and checkout_time:
        duration = (checkout_time - checkin_time).total_seconds() / 3600
        price = duration * 10
        return round(price, 2) 
    else:
        return 0.00  # Return 0 if times are missing
    
@csrf_exempt  # Exempts this view from CSRF protection (use with caution)
@api_view(["POST"])
def check_in(request,user_id ,branch_id):
    if (request.method == "POST"):
        client = User.objects.get(id=user_id)
        branch= Branch.objects.get(id = branch_id)
        check_in = datetime.now()

        history_data={
            'client_id ':client.id,
            'branch_id ':branch.id,
            'check_in':check_in,
        }
    serializer = HistorySerializer(data=history_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(["PUT"])
def check_out(request, user_id, branch_id):
    if request.method == 'PUT':
        client = User.objects.get(id=user_id)
        branch = Branch.objects.get(id=branch_id)
        
        # Find the history entry to check out
        history = History.objects.filter(client_id=client, branch_id=branch, checkout_time__isnull=True).first()
        if history:
            history.checkout_time = datetime.now()
            history_data = {
                'price': calculate_price(history.checkin_time, history.checkout_time),
            }
            serializer = HistorySerializer(history, data=history_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)

    return Response({'message': 'Invalid request method'}, status=405)

#get all history ,delete history , get history by specific checkin (data)get history by specific branch employees ,
