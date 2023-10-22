import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login
from .models import User

@csrf_exempt  # Use this decorator to disable CSRF protection for this view for simplicity (not recommended for production)
@require_http_methods(["POST"]) 
def add_user(request):
        try:
                data = json.loads(request.body.decode('utf-8'))  # Parse JSON data from the request
                age = data.get('age')
                age = int(age) if age and age.isdigit() else None
                

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

@csrf_exempt  
@require_http_methods(["GET"]) 
def get_all_users(request):
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
def get_user_by_id(request, user_id):
        try:
                user = User.objects.get(pk=user_id)
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
def update_user(request, user_id):
        pass

@csrf_exempt 
@require_http_methods(["DELETE"]) 
def delete_user(request, user_id):
        try:
                user = User.objects.get(pk=user_id)
                user.delete()
                return JsonResponse({'message': 'User deleted successfully'})
        except User.DoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=404)

@csrf_exempt 
@require_http_methods(["POST"])
def handel_login(request):
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