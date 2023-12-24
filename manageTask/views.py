from django.shortcuts import render
from django.http import HttpResponse
""" views """

def home(request):
    """ home view """
    return HttpResponse('this is home page')

