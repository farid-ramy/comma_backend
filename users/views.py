import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login
from .models import User

@csrf_exempt  # Use this decorator to disable CSRF protection for this view for simplicity (not recommended for production)
@require_http_methods(["POST"]) 
def addUser(request):
        try:

                data = json.loads(request.body.decode('utf-8'))  # Parse JSON data from the request
                age = data.get('age')
                age = int(age) if age and age.isdigit() else None
                
                required_field= ['first_name', 'last_name', 'password']
                for field in required_field:
                        if field not in data:
                                return JsonResponse({'error':"missing requried field:{field}"},status=400)

                         
                       
                email = data.get('email')
                if not email or not validate_email(email):
                        return JsonResponse({'error':"invalid email address"},status=400)

                if User.objects.filter(username=data.get('username')).exists():
                       return JsonResponse({'error': 'Username is already in use'}, status=400)
                if User.objects.filter(email=email).exists():
                       return JsonResponse({'error': 'Email address is already in use'}, status=400)
                if User.objects.filter(phone=data.get('phone')).exists():
                       return JsonResponse({'error': 'Phone number is already in use'}, status=400)
                user = User(
                        first_name=data['first_name'],
                        last_name=data['last_name'],
                        username=data.get('username'),
                        password=data.get('password'),
                        email=data.get('email'),
                        phone=data.get('phone'),
                        age=age,
                        job=data.get('job'),
                        address=data.get('address'),
                        role=data.get('role'),
                        national_id=data.get('national_id')
                )
                user.save()

                return JsonResponse({'message': 'User created successfully'})
        except json.JSONDecodeError as e:
                return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        
def validate_email(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError

    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

@csrf_exempt  
@require_http_methods(["GET"]) 
def getAllUsers(request):
        users = User.objects.all()
        user_list = []

        for user in users:
                user_data = {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'phone': user.phone,
                'age': user.age,
                'job': user.job,
                'address': user.address,
                'role': user.role,
                'national_id': user.national_id,}
                user_list.append(user_data)

        return JsonResponse({'users': user_list})

@csrf_exempt  
@require_http_methods(["GET"]) 
def getUserById(request, userId):
        try:
                user = User.objects.get(pk=userId)
                user_data = {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'phone': user.phone,
                'age': user.age,
                'job': user.job,
                'address': user.address,
                'role': user.role,
                'national_id': user.national_id,}

                return JsonResponse(user_data)
        except User.DoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=404)

@csrf_exempt
@require_http_methods(["PUT"])
def updateUser(request, user_id):
    try:

        user = User.objects.get(pk=user_id)

        data = json.loads(request.body.decode('utf-8'))

        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.email = data.get('email', user.email)
        user.phone = data.get('phone', user.phone)
        user.age = data.get('age', user.age)
        user.job = data.get('job', user.job)
        user.address = data.get('address', user.address)
        user.role = data.get('role', user.role)
        user.national_id = data.get('national_id', user.national_id)

        user.save()

        return JsonResponse({'message': 'User updated successfully'})
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    except json.JSONDecodeError as e:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)

@csrf_exempt 
@require_http_methods(["DELETE"]) 
def deleteUser(request, user_id):
        try:
                user = User.objects.get(pk=user_id)
                user.delete()
                return JsonResponse({'message': 'User deleted successfully'})
        except User.DoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=404)

@csrf_exempt 
@require_http_methods(["POST"])
def handelLogin(request):
        try:
                login_data = json.loads(request.body)
                username = login_data.get('username')
                password = login_data.get('password')

                # Authenticate the user
                user = authenticate(request, username=username, password=password)

                if user is not None:
                # Log the user in
                        login(request, user)
                        return JsonResponse({'message': 'Login successful'})
                else:
                        return JsonResponse({'error': 'Invalid credentials'}, status=401)

        except Exception as e:
                return JsonResponse({'error': 'Error during login', 'details': str(e)}, status=500)