from rest_framework import serializers
from .models import Employee, EmployeePerformance

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model= Employee
        fields= '__all__'

class EmployeePerformanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeePerformance
        fields = '__all__'