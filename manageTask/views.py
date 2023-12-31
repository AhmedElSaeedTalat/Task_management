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
from django.contrib.auth.models import User
from .sort import sort_values
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
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
        -- retrieve searched employee based on salary or username 
    """
    search_salary = json.load(request)
    key = search_salary['key']
    names = []
    employees = Employee.objects.all()
    """
        if key passed through post request is username
        -- usernames are sorted to determine root 4 the tree
        -- a tree is built from employees objects to nodes
        -- value received passed to tree to seach
        -- Return - username and salary found 
    """
    if key == 'username':
        seach_value = search_salary['search']
        users = User.objects.values_list('username', flat=True)
        users = list(users)
        sort_values(users, 0, len(users) - 1)
        mid = int(0 + (len(users) - 0) / 2)
        user_root = users[mid]
        root_node = Tree_Node()
        root_node.username = user_root
        root_node.salary = 0
        for node in employees:
            node = root_node.create_node(node)
            root_node.insert_node(node, root_node, 'username')
        found_node = root_node.search('username', root_node, seach_value, [])

    else:
        search = int(search_salary['search'])
        """ retrieve avarage salary and create root node with it"""
        avg = Employee.objects.aggregate(Avg("salary"))['salary__avg']
        root_node = Tree_Node()
        root_node.salary = avg
        root_node.username = 'root'

        """ create node from Employees queryset"""
        for node in employees:
            node = root_node.create_node(node)
            root_node.insert_node(node, root_node, 'salary')
        """ search for employee based on salary """
        found_node = root_node.search('salary', root_node, search, [])

    for node in found_node:
        names.append({'name': node.username, 'salary': node.salary})

    return JsonResponse({'data': names})


def view_employee(request):
    """ view each employee through linked-lists """
    employees = Employee.objects.all()
    employees_list = []
    for employee in employees:
        employee_dict = {}
        employee_dict['salary'] = str(employee.salary)
        employee_dict['taskCount'] = employee.total_taskCount
        employee_dict['user_name'] = employee.user.username
        employees_list.append(employee_dict)

    return render(request, 'employee.html', {'list_employees': json.dumps(employees_list)})

def delete_employee(request):
    """ deletes employee """
    user_id = request.POST['employee_id']
    user = User.objects.filter(pk=user_id)
    user.delete()
    messages.success(request, 'user got deleted')
    return redirect('EmployeeView')