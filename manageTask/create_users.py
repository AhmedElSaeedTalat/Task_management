""" create users through shell """
from django.contrib.auth.models import User
list_users = ['janit', 'Marcos', 'Marina', 'Sara', 'Marinho', 'Ahmed', 'Sharok', 'Mohammed', 'Anthony']
list_users = ['Jackson', 'Meervut', 'Andrew', 'Hatem', 'Karmen', 'Nesreen', 'Fahd', 'James', 'Jose']
list_users = ['fati', 'josephine', 'lorientes'] 

for user in list_users:
    usr = User.objects.create(username=user)
    usr.save()