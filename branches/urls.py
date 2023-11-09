from django.urls import path
from .views import branch_list, branch_detail, branch_create, branch_update, branch_delete

urlpatterns = [
    path('', branch_list, name='branch_list'),
    path('<int:branch_id>', branch_detail, name='branch_detail'),
    path('create', branch_create, name='branch_create'),
    path('<int:branch_id>/update', branch_update, name='branch_update'),
    path('<int:branch_id>/delete', branch_delete, name='branch_delete'),
]
