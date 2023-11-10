from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['PUT'])
def branch_update(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    serializer = BranchSerializer(instance=branch, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def branch_delete(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    serializer = BranchSerializer(branch)
    branch.delete()
    return Response(serializer.data)
