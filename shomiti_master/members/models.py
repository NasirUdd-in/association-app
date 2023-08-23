from django.db import models

# Create your models here.
# Employee Information model


class Employee(models.Model):
    admission_date = models.DateField()
    father_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    nid_number = models.CharField(max_length=20, blank=True, null=True)
    husband_or_wife_name = models.CharField(
        max_length=100, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.TextField()
    religion = models.CharField(max_length=50)
    note = models.TextField(blank=True, null=True)
    second_contact_number = models.CharField(
        max_length=20, blank=True, null=True)
    image = models.ImageField(
        upload_to='employee_images/', blank=True, null=True)

    def __str__(self):
        return self.name

# Granter Information model


class Granter(models.Model):
    name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    address = models.TextField()
    husband_or_wife_name = models.CharField(
        max_length=100, blank=True, null=True)
    shop = models.CharField(max_length=200, blank=True, null=True)
    religion = models.CharField(max_length=50)
    note = models.TextField(blank=True, null=True)
    second_contact_number = models.CharField(
        max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

# Login Information model


class EmployeeLogin(models.Model):
    LANGUAGE_CHOICES = (
        ('Bangla', 'Bangla'),
        ('English', 'English'),
    )

    ROLE_CHOICES = (
        ('member', 'Member'),
        ('employee', 'Employee'),
    )

    LOGIN_PERMISSION_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )

    user_name = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    login_permission = models.CharField(
        max_length=10, choices=LOGIN_PERMISSION_CHOICES, default='active')
    employee = models.OneToOneField(
        Employee, on_delete=models.CASCADE, blank=True, null=True)


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='images/')
