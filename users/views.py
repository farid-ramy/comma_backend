from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, CreateUserSerializer

# /api/users/create
@api_view(['POST'])
def create_user(request):
    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    
# /api/users/get
@api_view(['GET'])
def list_users(request):
    query_params = request.query_params
    query = {}
    for key, value in query_params.items():
        if not key or not value:
            return Response({"error": "Invalid query parameter provided."})
        query[key] = value

    try:
        users = User.objects.filter(**query)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)})

# /api/users/get/<int:user_id>
@api_view(['GET'])
def get_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

# /api/users/<int:user_id>/update
@api_view(['PUT'])
def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    serializer = CreateUserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

# /api/users/<int:user_id>/delete
@api_view(['DELETE'])
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return Response({'message': 'User deleted successfully'})

# /api/users/login
@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if username is None or password is None:
        return Response({'error': 'Please enter both username and password'})
    try:
        user = User.objects.get(username=username , password=password )
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except:
        return Response({'error': 'Wrong username or password'})