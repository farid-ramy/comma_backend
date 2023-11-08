from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BranchSerializer
from .models import Branch
from django.http import JsonResponse
from .models import Branch
from .serializers import BranchSerializer
from users.models import User
from users.serializers import UserSerializer

# /api/branches
def getAllBranches(request):
    branches = Branch.objects.all()
    branch_data = []
    for branch in branches:
        branch_serializer = BranchSerializer(branch)
        employees = User.objects.filter(workingin__branch_id=branch)
        employee_data = UserSerializer(employees, many=True)
        branch_details = branch_serializer.data
        branch_details["working_employees"] = employee_data.data
        branch_data.append(branch_details)
    return JsonResponse(branch_data, safe=False)


# /api/branches/<int:branchId>
@api_view(["GET"])
def getBranchById(request, branchId):
    try:
        branch = Branch.objects.get(pk=branchId)
        branch_data = []
        branch_serializer = BranchSerializer(branch)
        employees = User.objects.filter(workingin__branch_id=branch)
        employee_data = UserSerializer(employees, many=True)
        branch_data.append({
            'branch_details': branch_serializer.data,
            'working_employees': employee_data.data
        })
        return JsonResponse({'data': branch_data})
    except :
        return Response({'error': 'Branch not found'})


# /api/branches/add>
@csrf_exempt
@api_view(["POST"])
def addBranch(request):
    serializer = BranchSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


# /api/branches/delete/<int:branchId>
@api_view(["DELETE"])
def deleteBranch(request, branchId):
    try:
        branch = Branch.objects.get(pk=branchId)
        branch.delete()
        return Response({'message': 'Branch deleted successfully'})
    except:
        return Response({'error': 'Branch not found'})


# /api/branches/update/<int:branchId>
@api_view(["PUT"])
def updateBranch(request, branchId):
    try:
        branch = Branch.objects.get(pk=branchId)
        serializer = BranchSerializer(branch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    except :
        return Response({'error': 'Branch not found'})
    

