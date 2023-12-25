from django.forms import ModelForm
from .models import Employee
from django.contrib.auth.models import User
""" handle forms here """


class EmployeeForm(ModelForm):
    """ 
        model Form for employees to insert employee
    """
    class Meta:
        model = Employee
        fields = ('salary', 'user', 'bonus')

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)

        list_users = Employee.objects.values_list('user', flat=True)
        self.fields['user'].queryset = User.objects.exclude(pk__in=list_users)