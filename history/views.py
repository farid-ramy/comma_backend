from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import History
from .serializers import HistorySerializer
from datetime import datetime
from users.models import User
from branches.models import Branch
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist  # Import the exception


@api_view(["POST"])
def check_in(request, user_id, branch_id):
    if request.method == "POST":
        try:
            client = User.objects.get(id=user_id)
            branch = Branch.objects.get(id=branch_id)
            checkin_time = datetime.now()

            history_data = {
                'client_id': client.id,
                'branch_id': branch.id,
                'checkin_time': checkin_time,
            }
            serializer = HistorySerializer(data=history_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except ObjectDoesNotExist as e:
            # Handle the case where objects do not exist (e.g., client or branch not found)
            return Response({'message': 'Object does not exist'}, status=404)
        except Exception as e:
            # Handle other exceptions
            return Response({'message': 'Internal server error'}, status=500)
    return Response({'message': 'Invalid request method'}, status=405)
@api_view(["PUT"])
def check_out(request, user_id, branch_id):
    if request.method == 'PUT':
        try:
            client = User.objects.get(id=user_id)
            branch = Branch.objects.get(id=branch_id)
            
            # Find the history entry to check out
            history = History.objects.get(client_id=client, branch_id=branch, checkout_time__isnull=True)
            history.checkout_time = datetime.now()
            
            # Calculate the duration and price
            duration = (history.checkout_time - history.checkin_time).total_seconds() / 3600
            price = duration * 10
            
            history_data = {
                'checkout_time': history.checkout_time,
                'price': round(price, 2),
            }
            
            serializer = HistorySerializer(history, data=history_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except ObjectDoesNotExist as e:
            # Handle the case where objects do not exist (e.g., client or branch not found)
            return Response({'message': 'Object does not exist'}, status=404)
        except Exception as e:
            # Handle other exceptions
            return Response({'message': 'Internal server error'}, status=500)
    return Response({'message': 'Invalid request method'}, status=405)

#get all history ,delete history , get history by specific checkin (data)get history by specific branch employees ,

# price =100;discount =10%
#x=discount /100
#price *x
#
