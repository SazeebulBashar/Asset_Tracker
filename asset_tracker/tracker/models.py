from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name
    

class Device(models.Model):
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    condition = models.CharField(max_length=255, default='Good')
    checked_out = models.BooleanField(default=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        ordering = ['serial_number']

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    devices = models.ManyToManyField(Device, through='DeviceAssignment')

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['user']
        db_table = 'Employee'

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class DeviceAssignment(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)
    assigned_date = models.DateTimeField(null=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'DeviceAssignment'
        verbose_name_plural = 'DeviceAssignment'
        ordering = ['-updated_at']

    def __str__(self):
        if self.return_date:
            return f"{self.device.name} returned by {self.employee.user.get_username()} at: ({self.return_date.ctime()})"
        return f"{self.device.name} assigned to {self.employee.user.get_username()}, at: ({self.assigned_date.ctime()})"

    

