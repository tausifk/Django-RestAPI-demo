from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import EmployeeListView, EmployeeDetailView, UserCreateView, LoginView

# router = DefaultRouter()
# router.register('employees/', views.EmployeeViewSet, base_name='employees')

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('users/register/', UserCreateView.as_view(), name='user_create'),
    path('employees/', EmployeeListView.as_view(), name='employees'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name = 'employees_RUD'),    
]

# urlpatterns += router.urls


