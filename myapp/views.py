import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .models import Package

@csrf_exempt
@require_http_methods(["POST"])
def add_package(request):
    try:
       data = json.loads(request.body)
       package_name = data.get('name', '')
       if Package.objects.filter(name=package_name).exists():
            return JsonResponse({'error': 'A package with the same name already exists'}, status=400)
       price = data.get('price','')
       if not price.replace(".","",1).isdigit():
           return JsonResponse({'error': "invalid price must be an integer "}, status=400)

       package = Package(
            name=data['name'],
            description=data.get('description', ''),
            price=data['price'],
        )
       package.save()
       return JsonResponse({'message': 'Package created successfully'})
    except json.JSONDecodeError as e:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    

@csrf_exempt
@require_http_methods(["GET"])
def get_all_packages(request):
    packages = Package.objects.all()
    package_list = []
    for package in packages:
        package_data = {
            'id': package.id,
            'name': package.name,
            'description': package.description,
            'price': package.price,
        }
        package_list.append(package_data)
    return JsonResponse({'packages': package_list})


@csrf_exempt
@require_http_methods(["GET"])
def get_package_by_id(request, package_id):
    try:
        package = Package.objects.get(pk=package_id)
        package_data = {
            'id': package.id,
            'name': package.name,
            'description': package.description,
            'price': package.price,
        }
        return JsonResponse(package_data)
    except Package.DoesNotExist:
        return JsonResponse({'error': 'Package not found'}, status=404)
    

@csrf_exempt
@require_http_methods(["PUT"])
def update_package(request, package_id):
    try:
        package = Package.objects.get(pk=package_id)
        data = json.loads(request.body.decode('utf-8'))

        # Update package attributes
        package.name = data.get('name', package.name)
        package.description = data.get('description', package.description)
        package.price = data.get('price', package.price)
        package.save()

        return JsonResponse({'message': 'Package updated successfully'})
    except Package.DoesNotExist:
        return JsonResponse({'error': 'Package not found'}, status=404)
    except json.JSONDecodeError as e:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    


    
@csrf_exempt
@require_http_methods(["DELETE"])
def delete_package(request, package_id):
    try:
        package = Package.objects.get(pk=package_id)
        package.delete()
        return JsonResponse({'message': 'Package deleted successfully'})
    except Package.DoesNotExist:
        return JsonResponse({'error': 'Package not found'}, status=404)
# Create your views here.

# Create your views here.