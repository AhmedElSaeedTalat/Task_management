from rest_framework import serializers
from .models import Employee, Category, Task
from django.shortcuts import get_object_or_404
""" serializers """


class EmployeeSerializer(serializers.ModelSerializer):
    """ serializers for employess """
    class Meta:
        model = Employee
        fields = ('id', 'salary', 'user', 'bonus', 'total_taskCount')

class CategorySerializer(serializers.ModelSerializer):
    """ serializer for category """
    class Meta:
        model = Category
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    """ serializer for Task """
    class Meta:
        model = Task
        fields = '__all__'