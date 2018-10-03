from django.shortcuts import render
from .models import Employee, EmployeePerformance
from .serializers import EmployeeSerializer, EmployeePerformanceSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics

class EmployeeAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    # def get(self, request):
    #     employees = Employee.objects.all()
    #     serialzer = EmployeeSerializer(employees, many=True)
    #     return Response(serialzer.data)

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    # def get(self, request, pk):
    #     employee = get_object_or_404 (Employee, pk=pk)
    #     serialzer = EmployeeSerializer(employee)
    #     return Response(serialzer.data)

class Home(View):
    template_name = 'employee/home.html'

    def get(self, request):
        return render( request, self.template_name)

class EmployeePerformanceListView(generics.ListCreateAPIView):
    queryset = EmployeePerformance.objects.all()
    serializer_class = EmployeePerformanceSerializer

class EmployeePerformanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        queryset = EmployeePerformance.objects.filter(id=self.kwargs["pk"])
        return queryset
    serializer_class = EmployeePerformanceSerializer

class YearwisePerformanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        queryset = EmployeePerformance.objects.filter(id=self.kwargs["pk"]).filter(year__year=self.kwargs["year"])
        return queryset
    serializer_class = EmployeePerformanceSerializer

