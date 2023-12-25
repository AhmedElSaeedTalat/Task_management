from rest_framework import viewsets
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
""" module for rest views """


class EmployeeRestView(viewsets.ViewSet):
    """ Employee view class """
    def list(self, request):
        """ display all employees """
        if request.user.groups.filter(name='Manager').exists():
            queryset = Employee.objects.all()
            serializer = EmployeeSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response('not authorized to view')

    def post(self, request):
        """ 
            post employees
            -- post username and salary
            -- check if username exists 
            -- create employee object and
            -- relate it with the username passed
        """
        data = request.data
        user = get_object_or_404(User, username=data['user'])
        if hasattr(user, 'employee'):
            return Response('user has employee id generated')
        data['user'] = user.id
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            emp = Employee.objects.create(
                user = serializer.validated_data['user'],
                salary = serializer.validated_data['salary']
            )
            emp.save()
            return Response('Employee got created')
        else:
            return Response(serializer.errors)