from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import BranchSerializer
from .models import Branch

@api_view(["POST"])
def addBranch(request):
    # Serialize the request data using BranchSerializer
    serializer = BranchSerializer(data=request.data)
    if serializer.is_valid():
        # Save the validated data to create a new Branch object
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


    
@api_view(["DELETE"])
def deleteBranch(request,branchId):
    try:
        branch= Branch.objects.get(pk=branchId)
        branch.delete()
        return Response({'branch deleted successfully'})
    except Branch.DoesNotExist:
        return Response({'error': 'branch not found'}, status= status.HTTP_404_NOT_FOUND)
    
        


