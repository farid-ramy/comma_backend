from rest_framework import serializers
from .models import History

class HistorySerializer(serializers.ModelSerializer):
    client_id = serializers.SerializerMethodField()
    employee_id = serializers.SerializerMethodField()
    branch_id = serializers.SerializerMethodField()

    class Meta:
        model = History
        fields = [
            'id', 'client_id', 'employee_id', 'branch_id',
            'check_in_time', 'check_out_time', 'payment'
        ]

    def get_client_id(self, history):
        return {
            "id": history.client_id.id,
            "role": history.client_id.role,
            "first_name": history.client_id.first_name,
            "last_name": history.client_id.last_name,
            "username": history.client_id.username,
            "password": history.client_id.password,
            "phone": history.client_id.phone,
            "email": history.client_id.email,
            "national_id": history.client_id.national_id,
            "age": history.client_id.age,
            "job": history.client_id.job,
            "address": history.client_id.address,
            "created_at": history.client_id.created_at.isoformat(),
            "modified_at": history.client_id.modified_at.isoformat(),
        }

    def get_employee_id(self, history):
        return {
            "id": history.employee_id.id,
            "role": history.employee_id.role,
            "first_name": history.employee_id.first_name,
            "last_name": history.employee_id.last_name,
        }

    def get_branch_id(self, history):
        return {
            "name":history.branch_id.name
        }
