from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from .models import User

# /api/users/add
@csrf_exempt 
@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:

        return Response(serializer.errors)


# /api/users/get_users
@api_view(["GET"])
def getAllUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


# /api/users/get_users/clients
@api_view(["GET"])
def getAllClients(req):
    clients = User.objects.filter(role="client")
    serializer = UserSerializer(clients, many=True)
    return Response(serializer.data)


# /api/users/get_users/admins
@api_view(["GET"])
def getAllAdmins(req):
    employees = User.objects.filter(role="admin")
    serializer = UserSerializer(employees, many=True)
    return Response(serializer.data)


# /api/users/get_users/managers
@api_view(["GET"])
def getAllManagers(req):
    employees = User.objects.filter(role="manager")
    serializer = UserSerializer(employees, many=True)
    return Response(serializer.data)


# /api/users/update/<int:userId>
@api_view(['PUT'])
def updateUser(request, userId):
    try:
        user = User.objects.get(pk=userId)
    except:
        return Response({'error': 'User not found'})

    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


# /api/users/delete/<int:userId>
@api_view(['DELETE'])
def deleteUser(request, userId):
    try:
        user = User.objects.get(pk=userId)
        user.delete()
        return Response({'message': 'User deleted successfully'})
    except:
        return Response({'error': 'User not found'})


# /api/users/handel_login
@csrf_exempt  
@api_view(['POST'])
def handleLogin(request):
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


# /api/users/get_users/<int:userId>
@api_view(["GET"])
def getUserById(request, userId):
    try:
        user = User.objects.get(pk=userId)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except:
        return Response({'error': 'User not found'})







