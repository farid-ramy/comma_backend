from django.shortcuts import render
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .models import Branch


# @csrf_exempt
# @require_http_methods(["POST"])
# def add_branch(request):
#     try:
#         data=json.loads(request.body)
#         bracchname= data.get('name','')
#         if Branch.objects.filter(name=bracchname).exists():
#             return JsonResponse({"error":"a branch with the same name already exists"})
        


#     except:

# # Create your views here.



