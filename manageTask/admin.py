from django.contrib import admin
from .models import Category
from .models import Task
from .models import Employee
from .models import Recognitions
from .models import Comments
from .models import History

# Register your models here.
admin.site.register(Category)
admin.site.register(Task)
admin.site.register(Employee)
admin.site.register(Recognitions)
admin.site.register(Comments)
admin.site.register(History)
