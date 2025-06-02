from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Employee, Department


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['user', 'first_name', 'last_name', 'employee_id', 'department', 'job_title', 'gender', 'contract_type', 'address', 'position']
        read_only_fields = ('user', 'employee_id' )
