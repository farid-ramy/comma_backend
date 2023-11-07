from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import BranchSerializer
from .models import Branch

# View to get all branches
@api_view(["GET"])
def getAllBranches(request):
    # Retrieve all Branch objects from the database
    branches = Branch.objects.all()
    
    # Serialize the data using BranchSerializer
    serializer = BranchSerializer(branches, many=True)
    
    # Return the serialized data as a response
    return Response(serializer.data)

# View to get a branch by its ID
@api_view(["GET"])
def getBranchById(request, branchId):
    try:
        # Attempt to retrieve a specific Branch by its ID
        branch = Branch.objects.get(pk=branchId)
        
        # Serialize the found branch and return it as a response
        serializer = BranchSerializer(branch)
        return Response(serializer.data)
    except Branch.DoesNotExist:
        # Handle the case where the branch with the specified ID is not found
        return Response({'error': 'Branch not found'}, status=status.HTTP_404_NOT_FOUND)

# View to add a new branch
@csrf_exempt  # Exempts this view from CSRF protection (use with caution)
@api_view(["POST"])
def addBranch(request):
    # Serialize the request data using BranchSerializer
    serializer = BranchSerializer(data=request.data)
    
    if serializer.is_valid():
        # Save the validated data to create a new Branch object
        serializer.save()
        
        # Return the newly created branch data as a response with a 201 status code
        return Response(serializer.data)
    else:
        # Return validation errors with a 400 status code if data is not valid
        return Response(serializer.errors)

# View to delete a branch by its ID
@api_view(["DELETE"])
def deleteBranch(request, branchId):
    try:
        # Attempt to retrieve a specific Branch by its ID
        branch = Branch.objects.get(pk=branchId)
        
        # Delete the found branch
        branch.delete()
        
        # Return a success message as a response
        return Response({'message': 'Branch deleted successfully'})
    except Branch.DoesNotExist:
        # Handle the case where the branch with the specified ID is not found
        return Response({'error': 'Branch not found'}, status=status.HTTP_404_NOT_FOUND)

# View to update a branch by its ID
@api_view(["PUT"])
def updateBranch(request, branchId):
    try:
        # Attempt to retrieve a specific Branch by its ID
        branch = Branch.objects.get(pk=branchId)
    except Branch.DoesNotExist:
        # Handle the case where the branch with the specified ID is not found
        return Response({'error': 'Branch not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        # Serialize and update the branch with the request data
        serializer = BranchSerializer(branch, data=request.data)
        if serializer.is_valid():
            # Save the updated data
            serializer.save()
            
            # Return the updated branch data with a 201 status code
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Return validation errors with a 400 status code if data is not valid
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
