from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Kitchen
from .serializers import KitchenSerializer
# # from .models import Branch 
# from .serializers import ProductSerializer,BranchSerializer
from .models import Branch
from .serializers import ProductSerializer,BranchSerializer


@api_view(['POST'])
def addKitchenForBranch(request, branch_id):
    try:
        # Retrieve the branch based on the branch_id
        branch = Branch.objects.get(pk=branch_id)

        # Create a KitchenSerializer instance with the data from the request
        serializer = KitchenSerializer(data=request.data)

        if serializer.is_valid():
            # Save the kitchen to the database, associating it with the branch
            serializer.save(branch=branch)

            # Return the serialized kitchen data with a status of 201 (Created)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Return validation errors with a status of 400 (Bad Request)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Branch.DoesNotExist:
        # Return an error response if the branch does not exist
        return Response({'error': 'Branch not found'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def addProductToKitchen(request, branch_id, kitchen_id):
    try:
        # Retrieve the branch based on the branch_id
        branch = Branch.objects.get(pk=branch_id)

        # Retrieve the kitchen based on the kitchen_id
        kitchen = Kitchen.objects.get(pk=kitchen_id)

        # Ensure that the kitchen is associated with the specified branch
        if kitchen.branch == branch:
            # Create a ProductSerializer instance with the data from the request
            serializer = ProductSerializer(data=request.data)

            if serializer.is_valid():
                # Save the product to the database, associating it with the kitchen
                serializer.save(kitchen=kitchen)

                # Return the serialized product data with a status of 201 (Created)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                # Return validation errors with a status of 400 (Bad Request)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Return an error response if the specified kitchen is not associated with the branch
            return Response({'error': 'Kitchen is not associated with the specified branch'}, status=status.HTTP_400_BAD_REQUEST)
    except Branch.DoesNotExist:
        # Return an error response if the branch does not exist
        return Response({'error': 'Branch not found'}, status=status.HTTP_404_NOT_FOUND)
    except Kitchen.DoesNotExist:
        # Return an error response if the kitchen does not exist
        return Response({'error': 'Kitchen not found'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def getBranchWithKitchen(request, branch_id, kitchen_id):
    try:
        # Retrieve the branch based on the branch_id
        branch = Branch.objects.get(pk=branch_id)

        # Retrieve the kitchen based on the kitchen_id
        kitchen = Kitchen.objects.get(pk=kitchen_id)

        # Check if the kitchen is associated with the specified branch
        if kitchen.branch == branch:
            # Serialize the branch and kitchen data
            branch_serializer = BranchSerializer(branch)
            kitchen_serializer = KitchenSerializer(kitchen)

            # Create a dictionary containing both branch and kitchen data
            result = {
                'branch': branch_serializer.data,
                'kitchen': kitchen_serializer.data,
            }

            # Return the serialized data
            return Response(result, status=status.HTTP_200_OK)
        else:
            # Return an error response if the specified kitchen is not associated with the branch
            return Response({'error': 'Kitchen is not associated with the specified branch'}, status=status.HTTP_400_BAD_REQUEST)
    except Branch.DoesNotExist:
        # Return an error response if the branch does not exist
        return Response({'error': 'Branch not found'}, status=status.HTTP_404_NOT_FOUND)
    except Kitchen.DoesNotExist:
        # Return an error response if the kitchen does not exist
        return Response({'error': 'Kitchen not found'}, status=status.HTTP_404_NOT_FOUND)