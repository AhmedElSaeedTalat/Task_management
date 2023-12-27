from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm
from django.core.exceptions import ValidationError
from django.db.models import Avg
from .tree import Tree_Node
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
""" views """

def home(request):
    """ home view """
    return HttpResponse('this is home page')

class EmployeeView(View):
    """ employee View """
    def get(self, request):
        """ display all Employees """
        if request.user.groups.filter(name='Manager').exists():
            form = EmployeeForm()
            employees = Employee.objects.all()
            data = {'form': form, 'emp': employees}
            return render(request, 'employees.html', {'data': data})
        else:
            return HttpResponse('not authorized to view')
    
    def post(self, request):
        """ insert new employee """
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('data saved')
        else:
            raise ValidationError('not valid')
        
@csrf_exempt
def search_employee(request):
    """ 
        function to search employee based on salary
        -- retrieve all employees with the relevant salary 
    """
    search_salary = json.load(request)
    search = int(search_salary['search'])
    # print(search_salary['search'])
    names = []
    employees = Employee.objects.all()
    """ retrieve avarage salary and create root node with it"""
    avg = Employee.objects.aggregate(Avg("salary"))['salary__avg']
    root_node = Tree_Node()
    root_node.salary = avg
    root_node.username = 'root'

    """ create node from Employees queryset"""
    for node in employees:
        node = root_node.create_node(node)
        root_node.insert_node(node, root_node)
    """ search for employee based on salary """
    found_node = root_node.search(root_node, search, [])

    for node in found_node:
        names.append(node.username)

    return JsonResponse({'data': names})

    





