from django.contrib import admin
from .models import Employee, Granter, EmployeeLogin, Hotel
# Register your models here.
admin.site.register(Employee)
admin.site.register(Granter)
admin.site.register(EmployeeLogin)
admin.site.register(Hotel)
