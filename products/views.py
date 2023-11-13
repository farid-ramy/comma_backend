from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import products
from .serializers import CreateProductSerializer
from rest_framework import status
from .models import Branch
# /api/products/create_product
@api_view(["POST"])
def create_product(request, branchId):
    try:
        branch = Branch.objects.get(pk=branchId)
        product = products(branch_id=branch)
        serializer = CreateProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Branch.DoesNotExist:
        return Response({'error': 'Branch not found'}, status=status.HTTP_404_NOT_FOUND)

# /api/products/<int:productId>
@api_view(["GET"])
def get_product(request, branchId, productId):
    try:
        product = products.objects.get(branch_id=branchId, pk=productId)
        serializer = CreateProductSerializer(product)
        return Response(serializer.data)
    except products.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
# /api/products
@api_view(["GET"])
def list_products(request, branchId):
    query_params = request.query_params
    query = {"branch_id": branchId}

    for key, value in query_params.items():
        if not key or not value:
            return Response({"error": "Invalid query parameter provided."})
        query[key] = value

    try:
        products_in_branch = products.objects.filter(**query)
        if products_in_branch.exists():
            serializer = CreateProductSerializer(products_in_branch, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'No products found in the branch'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)})

# /api/products/<int:productId>/update
@api_view(["PUT"])
def update_product(request, productId,branchId):
    try:
        product= products.objects.get(branch_id= branchId,pk= productId)
    except products.DoesNotExist:
        return Response({'error':'product isnot found '},status=status.HTTP_404_NOT_FOUND)
    if request.method=="PUT":
        serializer=CreateProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status= status.HTTP_404_NOT_FOUND)
        
# /api/products/<int:productId>/delete
@api_view(['DELETE'])
def delete_product(request, branchId, productId):
    try:
        product = products.objects.get(branch_id=branchId, pk=productId)
        product.delete()
        return Response({'message': 'Product deleted successfully'})
    except products.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

             
        
        
        
                   