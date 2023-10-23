from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import PackageSerializer
from .models import Package

# Define an API view to retrieve all Package objects
@api_view(["GET"])
def getAllPackages(request):    
    # Retrieve all Package objects from the database
    packages = Package.objects.all()
    # Serialize the data using PackageSerializer
    serializer = PackageSerializer(packages, many=True)
    # Return the serialized data in the response
    return Response(serializer.data)

# Define an API view to retrieve a Package object by its ID
@api_view(["GET"])
def getPackageById(request, packageId):
    try:
        # Attempt to retrieve a Package by its primary key (ID)
        package = Package.objects.get(pk=packageId)
        # Serialize the retrieved package
        serializer = PackageSerializer(package)
        # Return the serialized package data
        return Response(serializer.data)
    except Package.DoesNotExist:
        # Return a 404 error response if the package is not found
        return Response({'error': 'Package not found'}, status=status.HTTP_404_NOT_FOUND)


@csrf_exempt # Disable CSRF protection for the following view (for demonstration purposes)
# Define an API view to add a new Package
@api_view(["POST"])
def addPackage(request):
    # Serialize the data from the request using PackageSerializer
    serializer = PackageSerializer(data=request.data)

    if serializer.is_valid():
        # If the data is valid, save the new Package
        package = serializer.save()
        # Return the serialized data with a 201 status code (Created)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        # Return validation errors if the data is invalid
        return Response(serializer.errors)

# Define an API view to update an existing Package
@api_view(["PUT"])
def updatePackage(request, packageId):
    try:
        # Attempt to retrieve the existing Package by its ID
        package = Package.objects.get(pk=packageId)
    except Package.DoesNotExist:
        # Return a 404 error response if the package is not found
        return Response({'error': 'Package not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        # Serialize the existing Package with the updated data from the request
        serializer = PackageSerializer(package, data=request.data)
        if serializer.is_valid():
            # If the data is valid, save the updated Package
            serializer.save()
            # Return the updated data with a 200 status code (OK)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Return validation errors with a 400 status code (Bad Request) if the data is invalid
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Define an API view to delete a Package by its ID
@api_view(["DELETE"])
def deletePackage(request, packageId):
    try:
        # Attempt to retrieve the Package by its ID
        package = Package.objects.get(pk=packageId)
        # Delete the Package
        package.delete()
        # Return a success message with a 204 status code (No Content)
        return Response({'message': 'Package deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Package.DoesNotExist:
        # Return a 404 error response if the package is not found
        return Response({'error': 'Package not found'}, status=status.HTTP_404_NOT_FOUND)
