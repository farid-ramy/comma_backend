from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ProductSerializer
from .models import products


#api/products/getproducts
@api_view(["GET"])
def getAllProducts(request):
    product = products.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)

#api/products/getproduct/<int:productId>
@api_view(["GET"])
def getProductById(request, productId):
    try:
        product = products.objects.get(pk=productId)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except products.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

# /api/products/add
@api_view(["POST"])
def addProduct(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        product = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors)

#/api/products/update/<int:productId>
@api_view(["PUT"])
def updateProduct(request, productId):
    try:
        product = products.objects.get(pk=productId)
    except products.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#/api/products/delete/<int:productId>
@api_view(["DELETE"])
def deleteProduct(request, productId):
    try:
        product = products.objects.get(pk=productId)
        product.delete()
        return Response({'message': 'Product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except products.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
