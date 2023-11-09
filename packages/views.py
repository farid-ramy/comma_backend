from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import PackageSerializer
from .models import Package

#api/packages/getpackages
@api_view(["GET"])
def getAllPackages(request):
    package = Package.objects.all()
    serializer = PackageSerializer(package, many=True)
    return Response(serializer.data)

#api/packages/getpackage/<int:packageId>
@api_view(["GET"])
def getPackageById(request, packageId):
    try:
        package = Package.objects.get(pk=packageId)
        serializer = PackageSerializer(package)
        return Response(serializer.data)
    except Package.DoesNotExist:
        return Response({'error': 'Package not found'}, status=status.HTTP_404_NOT_FOUND)

 # /api/packages/add
@api_view(["POST"])
def addPackage(request):
    serializer = PackageSerializer(data=request.data)

    if serializer.is_valid():
        package = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors)

#/api/packages/update/<int:packageId>
@api_view(["PUT"])
def updatePackage(request, packageId):
    try:
        package = Package.objects.get(pk=packageId)
    except Package.DoesNotExist:
        return Response({'error': 'Package not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PackageSerializer(package, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#/api/packages/delete/<int:packageId>
@api_view(["DELETE"])
def deletePackage(request, packageId):
    try:
        package = Package.objects.get(pk=packageId)
        package.delete()
        return Response({'message': 'Package deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Package.DoesNotExist:
        return Response({'error': 'Package not found'}, status=status.HTTP_404_NOT_FOUND)

#/api/packages/offer/<int:packageId>
@api_view(["PUT"])
def offeroption(request, packageId):
    try:
        package= Package.objects.get(pk=packageId)
    except Package.DoesNotExist:
        return Response({'error': 'Package not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method =="PUT":
        serializer=PackageSerializer(package,data=request.data, partial=True)
        if serializer.is_valid():
            new_offer = serializer.validated_data.get('offer')
            if new_offer is not None:
                if new_offer>=0 and new_offer<=100:
                    discount = (new_offer/100)*package.price
                    package.offer=new_offer
                    package.price =package.price-discount 
                    package.save()
                    serializer= PackageSerializer(package)
                    return Response(serializer.data,status=status.HTTP_200_OK)
                else:
                    return Response ({"error ":"invalid offer value "},status=status.HTTP_400_BAD_REQUEST)
                
            else:
                return Response ({"error ":"you should enter a value "},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response ({"error ": serializer.errors},status=status.HTTP_400_BAD_REQUEST)  
 #api/packages/edit/<int:packageId>
@api_view(["PUT"])
def editoffer (request , packageId):
    try :
        package= Package.objects.get(id=packageId)
    except Package.DoesNotExist:
         return Response({'error': 'Package not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method =='PUT':
        serializer=PackageSerializer(package,data=request.data, partial=True)
        if  serializer.is_valid():
            new_offer = serializer.validated_data.get('offer')
            if new_offer is not None:
                if new_offer>=0 and new_offer<=100:
                    discount = (new_offer/100)*package.price
                    package.offer=new_offer
                    package.price =package.price-discount 
                    package.save()
                    serializer= PackageSerializer(package)
                    return Response(serializer.data,status=status.HTTP_200_OK)
                else:
                    return Response ({"error ":"invalid offer value "},status=status.HTTP_400_BAD_REQUEST)
                
            else:
                return Response ({"error ":"you should enter a value "},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response ({"error ": serializer.errors},status=status.HTTP_400_BAD_REQUEST)  
#api/packages/deleteoffer/<int:packageId>
@api_view(["DELETE"])
def delete_offer(request, packageId):
    try:
        package = Package.objects.get(id= packageId)
    except Package.DoesNotExist:
                 return Response({'error': 'Package not found'}, status=status.HTTP_404_NOT_FOUND)
    if package.offer is not None:
        package.offer= None
        package.price= package.price
        package.save()

        serializer= PackageSerializer(package)
        return Response({'message':'offer was deleted successfully','package':serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({'error':'no offer to delete was found'}, status=status.HTTP_400_BAD_REQUEST)
    
    