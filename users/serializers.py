from rest_framework import serializers
from users.models import User
from branches.models import Branch

class UserSerializer(serializers.ModelSerializer):
    branch_id = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'role', 'first_name', 'last_name', 'username', 'password',
            'phone', 'email', 'national_id', 'age', 'job', 'address',
            'created_at', 'modified_at', 'branch_id'
        ]

    def get_branch_id(self, user):
        branch = user.working_employees.first()
        return branch.id if branch else None
