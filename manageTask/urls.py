from django.urls import path, include
from . import views
from . import restViews 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', restViews.EmployeeRestView, basename='employees')
router.register('categories', restViews.CategoryView, basename='categories')
router.register('task', restViews.TaskView, basename='task')
""" views in url page """
urlpatterns = [
    path('employees/', views.EmployeeView.as_view(), name='EmployeeView'),
    path('api/', include(router.urls)),
    path('search-employee/', views.search_employee, name='search-employee'),
    path('employee/', views.view_employee, name='employee'),
    path('delete/', views.delete_employee, name='delete') 
]