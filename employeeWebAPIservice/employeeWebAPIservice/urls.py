"""employeeWebAPIservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employee import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='home'),
    path("employees/", views.EmployeeAPIView.as_view(), name="employees_list"),    
    path("employees/<int:pk>/", views.EmployeeDetailView.as_view(), name="employees_detail"),
    path("performance/", views.EmployeePerformanceListView.as_view(), name="performance_list"),
    # path("performance/<int:pk>/", views.EmployeeDetailView.as_view(), name="employees_detail"),
    path("employees/<int:pk>/performance/", views.EmployeePerformanceDetailView.as_view(), name="performance_details"),
    path("employees/<int:pk>/performance/<int:year>/", views.YearwisePerformanceDetailView.as_view(), name="performance_details"),    
]

urlpatterns = format_suffix_patterns(urlpatterns)
