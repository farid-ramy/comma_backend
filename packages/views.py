from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Package
from .serializers import PackageSerializer, CreatePackageSerializer

# /api/packages/create_package
@api_view(['POST'])
def create_package(request):
    serializer = CreatePackageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    
# /api/packages
@api_view(['GET'])
def list_packages(request):
    query_params = request.query_params
    query = {}
    for key, value in query_params.items():
        if not key or not value:
            return Response({"error": "Invalid query parameter provided."})
        query[key] = value

    try:
        packages = Package.objects.filter(**query)
        serializer = PackageSerializer(packages, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)})

# /api/packages/<int:package_id>
@api_view(['GET'])
def get_package(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    serializer = PackageSerializer(package)
    return Response(serializer.data)

# /api/packages/<int:package_id>/update
@api_view(['PUT'])
def update_package(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    serializer = CreatePackageSerializer(package, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

# /api/packages/<int:package_id>/delete
@api_view(['DELETE'])
def delete_package(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    package.delete()
    return Response({'message': 'Package deleted successfully'})
