# Generated by Django 4.2.8 on 2023-12-24 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Recognitions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('status', models.BooleanField(default=False)),
                ('priority', models.BooleanField(default=False)),
                ('due_date', models.DateField()),
                ('category', models.ManyToManyField(to='manageTask.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=200)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='manageTask.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
