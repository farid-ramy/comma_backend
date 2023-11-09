# serializers.py
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
            "id": history.client.id,
            "role": history.client.role,
            "first_name": history.client.first_name,
            "last_name": history.client.last_name,
            "username": history.client.username,
            "password": history.client.password,
            "phone": history.client.phone,
            "email": history.client.email,
            "national_id": history.client.national_id,
            "age": history.client.age,
            "job": history.client.job,
            "address": history.client.address,
            "created_at": history.client.created_at.isoformat(),
            "modified_at": history.client.modified_at.isoformat(),
        }

    def get_employee_id(self, history):
        return history.employee.id

    def get_branch_id(self, history):
        return history.branch.id
