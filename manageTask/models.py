from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
""" models classes """


class Category(models.Model):
    """ creating model for categories """
    name = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=500, null=False)

class Employee(models.Model):
    """ create model for tasks """
    salary = models.DecimalField(decimal_places=2, max_digits=65)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee')
    task_count = models.IntegerField(default=0)
    total_taskCount = models.IntegerField(default=0)
    bonus = models.DecimalField(decimal_places=2, max_digits=65, default=0.00)

    def increment_task(self):
        """ 
            function to increment tasks
            -- for each 400 completed task add bonus
            -- reset count in total_count after each 400
            -- store total completed in total_taskCount
        """
        self.task_count += 1
        self.total_taskCount += 1
        if self.task_count == 400:
            self.bonus += self.salary * 0.02
            self.task_count = 0
        
    def __str__(self):
        """ string representation """
        return str(self.user)

class Task(models.Model):
    """ create model for tasks """
    title = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=500, null=False)
    status = models.BooleanField(default=False)
    priority = models.BooleanField(default=False)
    due_date = models.DateField(null=False)
    category = models.ManyToManyField(Category)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='task', default=0)

class Recognitions(models.Model):
    """ recongnitions """
    name = models.CharField(max_length=200, null=True)


class Comments(models.Model):
    """ create comments model for relevant tasks """
    comment = models.CharField(max_length=500, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comment')


class History(models.Model):
    """ creating model for categories """
    action = models.CharField(max_length=200, null=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='history')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='history', default=0)
    date = models.DateField(default=timezone.now)