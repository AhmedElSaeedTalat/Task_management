# Generated by Django 4.2.8 on 2023-12-24 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manageTask', '0002_employee_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='Employee_id',
        ),
    ]
