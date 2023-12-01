from django.urls import path
from .views import list_branches, get_branch, create_branch, update_branch, delete_branch

urlpatterns = [
    path('create', create_branch.as_view(), name='create_branch'),
    path('', list_branches.as_view(), name='list_branches'),
    path('<int:branch_id>', get_branch.as_view(), name='get_branch'),
    path('<int:branch_id>/update', update_branch.as_view(), name='update_branch'),
    path('<int:branch_id>/delete', delete_branch.as_view(), name='delete_branch'),
]
