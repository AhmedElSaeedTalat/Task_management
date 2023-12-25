from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from .forms import EmployeeForm
from django.core.exceptions import ValidationError
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
            return render(request, 'employees.html', {'form': form})
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


