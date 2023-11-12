from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Branch
from .serializers import BranchSerializer, CreateBranchSerializer

# /api/branches/create
@api_view(['POST'])
def branch_create(request):
    serializer = CreateBranchSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

# /api/branches
@api_view(['GET'])
def list_branches(request):
    branches = Branch.objects.all()
    serializer = BranchSerializer(branches, many=True)
    return Response(serializer.data)

# /api/branches/<int:branch_id>
@api_view(['GET'])
def get_branch(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    serializer = BranchSerializer(branch)
    return Response(serializer.data)

# /api/branches/<int:branch_id>/update
@api_view(['PUT'])
def update_branch(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    serializer = CreateBranchSerializer(instance=branch, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

# /api/branches/<int:branch_id>/delete
@api_view(['DELETE'])
def delete_branch(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    branch.delete()
    return Response({'message': 'User deleted successfully'})
