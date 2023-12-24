""" create users through shell """
from django.contrib.auth.models import User
list_users = ['janit', 'Marcos', 'Marina', 'Sara', 'Marinho', 'Ahmed', 'Sharok', 'Mohammed', 'Anthony']
for user in list_users:
    usr = User.objects.create(username=user)
    usr.save()