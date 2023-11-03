from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserSerializer
from .models import User

# Get all users
@api_view(["GET"])
def getAllUsers(request):
    # Retrieve all user objects from the database
    users = User.objects.all()
    # Serialize the user objects using the UserSerializer
    serializer = UserSerializer(users, many=True)
    # Return the serialized data as a JSON response
    return Response(serializer.data)

# Get all clients
@api_view(["GET"])
def getAllClients(req):
    # Use the filter method to get all users with the role "client"
    clients = User.objects.filter(role="client")
    # Serialize the clients objects using the UserSerializer
    serializer = UserSerializer(clients, many=True)
    # Return the serialized data as a JSON response
    return Response(serializer.data)

# Get all employees
@api_view(["GET"])
def getAllEmployees(req):
    # Use the filter method to get all users with the role "employee"
    employees = User.objects.filter(role="employee")
    # Serialize the employees objects using the UserSerializer
    serializer = UserSerializer(employees, many=True)
    # Return the serialized data as a JSON response
    return Response(serializer.data)

# Get a user by their ID
@api_view(["GET"])
def getUserById(request, userId):
    try:
        # Try to retrieve a user by their primary key (ID)
        user = User.objects.get(pk=userId)
        # Serialize the user object using the UserSerializer
        serializer = UserSerializer(user)
        # Return the serialized user data as a JSON response
        return Response(serializer.data)
    except User.DoesNotExist:
        # Return an error response if the user does not exist
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

# Create a new user
@csrf_exempt  # Disables CSRF protection (for demonstration purposes only)
@api_view(['POST'])
def addUser(request):
    # Create a UserSerializer instance with the data from the request
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        # Save the user to the database
        user = serializer.save()
        # Return the serialized user data with a status of 201 (Created)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        # Return validation errors with a status of 400 (Bad Request)
        return Response(serializer.errors)

# Update user information
@api_view(['PUT'])
def updateUser(request, userId):
    try:
        # Try to retrieve the user to be updated
        user = User.objects.get(pk=userId)
    except User.DoesNotExist:
        # Return an error response if the user does not exist
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        # Create a UserSerializer instance with the user and the data from the request
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            # Save the updated user data
            serializer.save()
            # Return the updated user data with a status of 200 (OK)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Return validation errors with a status of 400 (Bad Request)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete a user
@api_view(['DELETE'])
def deleteUser(request, userId):
    try:
        # Try to retrieve the user to be deleted
        user = User.objects.get(pk=userId)
        # Delete the user
        user.delete()
        # Return a success message with a status of 204 (No Content)
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        # Return an error response if the user does not exist
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

# Handle user login
@csrf_exempt  # Disables CSRF protection (for demonstration purposes only)
@api_view(['POST'])
def handleLogin(request):
    # Extract the username and password from the request data
    username = request.data.get('username')
    password = request.data.get('password')

    if username is None or password is None:
        # Return an error response if username or password is missing
        return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.get(username=username , password=password )

    if user is not None:
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        # Return an error message if authentication fails
        return Response({'error': 'Login failed. Please check your credentials.'}, status=status.HTTP_401_UNAUTHORIZED)