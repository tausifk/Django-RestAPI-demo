from rest_framework import serializers
from django.contrib.auth.models import User 
from .models import Employee, PerformanceAppraisel
from rest_framework.authtoken.models import Token

class EmployeeSerializer(serializers.ModelSerializer):
    
    phoneNumber = serializers.IntegerField(source='phone_number')
    contactPreference = serializers.CharField(source='contact_preference')
    dateOfBirth = serializers.DateField(source='date_of_birth' , format='%d/%m/%Y', input_formats=None)
    isActive = serializers.BooleanField(source='is_active')
    photoPath = serializers.CharField(source='photo_path')

    class Meta:
        model = Employee
        fields = ('id','name', 'gender', 'email', 'phoneNumber', 'contactPreference', 'dateOfBirth', 'department', 'isActive', 'photoPath')


class PerformanceAppraiselSerializer(serializers.ModelSerializer):

    class Meta:
        model = PerformanceAppraisel
        fields = '__all__'   

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user 
    