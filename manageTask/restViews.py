from rest_framework import viewsets
from rest_framework.response import Response
from .models import Employee, Category, Task
from .serializers import EmployeeSerializer, CategorySerializer, TaskSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.decorators import action
""" module for rest views """



""" Employee Rest API Views """
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

    def retrieve(self, request, pk):
        employee = Employee.objects.filter(pk=pk).first()
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

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
    
    def delete(self, request, pk):
        """ function to delete employee """
        if request.user.groups.filter(name='Manager').exists():
            employee = get_object_or_404(Employee, pk=pk)
            user = get_object_or_404(User, pk=employee.user.id)
            employee.delete()
            user.delete()
            return Response('user got deleted')
        else:
            return Response('not authorized to view')

""" categories """
class CategoryView(viewsets.ViewSet):
    """ category class """
    def list(self, request):
        """ list all categories """
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """ retrieve categories """
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def post(self, request):
        """ post to categories """
        queryset = request.data
        serializer = CategorySerializer(data=queryset)
        if serializer.is_valid():
            cat = Category.objects.create(
                name = serializer.validated_data['name'],
                description = serializer.validated_data['description']
            )
            cat.save()
            return Response('category is created')
        else:
            return Response('incorrect data')
        
    def delete(self, request, pk):
        """ delete category """
        obj = get_object_or_404(Category, pk=pk)
        obj.delete()
        return Response('category got deleted')