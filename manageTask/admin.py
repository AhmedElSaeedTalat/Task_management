from django.contrib import admin
from .models import Category
from .models import Task
from .models import Employee
from .models import Recognitions
from .models import Comments
from .models import History

# Register your models here.
admin.register(Category)
admin.register(Task)
admin.register(Employee)
admin.register(Recognitions)
admin.register(Comments)
admin.register(History)
