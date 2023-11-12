from django.urls import path
from .views import list_branches, get_branch, create_branch, update_branch, delete_branch

urlpatterns = [
    path('create', create_branch, name='create_branch'),
    path('', list_branches, name='list_branches'),
    path('<int:branch_id>', get_branch, name='get_branch'),
    path('<int:branch_id>/update', update_branch, name='update_branch'),
    path('<int:branch_id>/delete', delete_branch, name='delete_branch'),
]
