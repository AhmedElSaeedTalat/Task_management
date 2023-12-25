from rest_framework import serializers
from .models import Employee
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
""" serializers """


class EmployeeSerializer(serializers.ModelSerializer):
    """ serializers for employess """
    class Meta:
        model = Employee
        fields = ('salary', 'user', 'bonus', 'total_taskCount')