from django.db import models

class Employee(models.Model):
    empCode = models.CharField(max_length=100)
    name = models.CharField(max_length=250)
    gender = models.CharField(max_length=10)
    salary = models.FloatField()
    dob = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class EmployeePerformance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    kra_points = models.IntegerField()
    promotion = models.BooleanField()
    increment = models.DecimalField(max_digits=5, decimal_places=2)
    year = models.DateField()

    def __str__(self):
       return str(self.employee)


