from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer, CreateUserSerializer
from django.contrib.auth import authenticate

# # /api/users/create
class create_user(APIView):
    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# #/api/users/get
class list_users(APIView):
    def get(self, request):
        query_params = request.query_params
        query = {}
        for key, value in query_params.items():
            if not key or not value:
                return Response({"error": "Invalid query parameter provided."}, status=status.HTTP_400_BAD_REQUEST)
            query[key] = value

        try:
            users = User.objects.filter(**query)
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# /api/users/get/<int:user_id>
class get_user(APIView):
    def get(self, request, branch_id):
        branch = get_object_or_404(User, id=branch_id)
        serializer = UserSerializer(branch)
        return Response(serializer.data)

# /api/users/<int:user_id>/update
class update_user(APIView):
    def put(self, request, user_id):
        user= get_object_or_404(User, id=user_id)
        serializer=CreateUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
# /api/users/<int:user_id>/delete
class delete_user(APIView):
    def delete(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return Response({'message': 'User deleted successfully'})

# # /api/users/login
class login_user(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({'error': 'Please enter both username and password'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response({'error': 'Wrong username or password'}, status=status.HTTP_401_UNAUTHORIZED)
