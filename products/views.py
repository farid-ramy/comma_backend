from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer, CreateProductSerializer

class CreateProduct(APIView):
    def post(self, request):
        serializer = CreateProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListProducts(APIView):
    def get(self, request):
        query_params = request.query_params
        query = {}
        for key, value in query_params.items():
            if not key or not value:
                return Response({"error": "Invalid query parameter provided."})
            query[key] = value

        try:
            products = Product.objects.filter(**query)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)})

class GetProduct(APIView):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class UpdateProduct(APIView):
    def put(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        serializer = CreateProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DeleteProduct(APIView):
    def delete(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        return Response({'message': 'Product deleted successfully'})
