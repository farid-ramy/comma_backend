from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Package
from .serializers import PackageSerializer, CreatePackageSerializer

class CreatePackage(APIView):
    def post(self, request):
        serializer = CreatePackageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListPackages(APIView):
    def get(self, request):
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

class GetPackage(APIView):
    def get(self, request, package_id):
        package = get_object_or_404(Package, id=package_id)
        serializer = PackageSerializer(package)
        return Response(serializer.data)

class UpdatePackage(APIView):
    def put(self, request, package_id):
        package = get_object_or_404(Package, id=package_id)
        serializer = CreatePackageSerializer(package, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DeletePackage(APIView):
    def delete(self, request, package_id):
        package = get_object_or_404(Package, id=package_id)
        package.delete()
        return Response({'message': 'Package deleted successfully'})
