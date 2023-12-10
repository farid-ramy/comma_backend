from django.urls import path
from .views import CreateBranch, ListBranches, GetBranch, UpdateBranch, DeleteBranch

urlpatterns = [
    path('create', CreateBranch.as_view(), name='create_branch'),
    path('', ListBranches.as_view(), name='list_branches'),
    path('<int:branch_id>', GetBranch.as_view(), name='get_branch'),
    path('<int:branch_id>/update', UpdateBranch.as_view(), name='update_branch'),
    path('<int:branch_id>/delete', DeleteBranch.as_view(), name='delete_branch'),
]
