from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Branch
from .serializers import BranchSerializer

@api_view(['GET'])
def branch_list(request):
    branches = Branch.objects.all()
    serializer = BranchSerializer(branches, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def branch_detail(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    serializer = BranchSerializer(branch)
    return Response(serializer.data)

@api_view(['POST'])
def branch_create(request):
    serializer = BranchSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def branch_update(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    serializer = BranchSerializer(instance=branch, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def branch_delete(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    branch.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
