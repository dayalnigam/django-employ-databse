from django.db import models
class Employee(models.Model):
	employeeid=models.CharField(max_length=30)
	employeename=models.CharField(max_length=30)
	employeegrade=models.CharField(max_length=30)
	employeesalary=models.CharField(max_length=30)
	class Meta:
		db_table="Employee"
		
# Create your models here.
