from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    phone_number = models.IntegerField()
    contact_preference = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    department = models.CharField(max_length=255)
    is_active = models.BooleanField()
    photo_path = models.CharField(verbose_name='photoPath', max_length=255)

    def __str__(self):
        return self.name



class PerformanceAppraisel(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    kra_rating = models.IntegerField()
    promotion = models.BooleanField()
    percentage_increment = models.DecimalField(max_digits=5, decimal_places=2)
    performance_year = models.DateField()