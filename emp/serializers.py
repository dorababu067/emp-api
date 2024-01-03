from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    reporting = serializers.StringRelatedField()

    class Meta:
        model = Employee
        fields = "__all__"
