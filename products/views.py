from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import products
from .serializers import ProductSerializer
from rest_framework import status
from .models import Branch

@api_view(["POST"])
def addProductToBranch(request, branchId):
    try:
        branch = Branch.objects.get(pk=branchId)
        product = products(branch_id=branch)
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Branch.DoesNotExist:
        return Response({'error': 'Branch not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def getProductById(request, branchId, productId):
    try:
        product = products.objects.get(branch_id=branchId, pk=productId)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except products.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(["GET"])
def getAllProductsInBranch(request, branchId):
    product = products.objects.filter(branch_id=branchId)
    if product.exists():
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({'error': 'No products found in the branch'}, status=status.HTTP_404_NOT_FOUND)
     
