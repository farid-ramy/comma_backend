from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Branch
from .serializers import BranchSerializer, CreateBranchSerializer

# /api/branches/create
class CreateBranch(APIView):
    def post(self, request):
        serializer = CreateBranchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /api/branches
class ListBranches(APIView):
    def get(self, request):
        branches = Branch.objects.all()
        serializer = BranchSerializer(branches, many=True)
        return Response(serializer.data)

# /api/branches/<int:branch_id>
class GetBranch(APIView):
    def get(self, request, branch_id):
        branch = get_object_or_404(Branch, id=branch_id)
        serializer = BranchSerializer(branch)
        return Response(serializer.data)

# /api/branches/<int:branch_id>/update
class UpdateBranch(APIView):
    def put(self, request, branch_id):
        branch = get_object_or_404(Branch, id=branch_id)
        serializer = CreateBranchSerializer(instance=branch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# /api/branches/<int:branch_id>/delete
class DeleteBranch(APIView):
    def delete(self, request, branch_id):
        branch = get_object_or_404(Branch, id=branch_id)
        branch.delete()
        return Response({'message': 'Branch deleted successfully'})
