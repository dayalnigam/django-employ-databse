from django.shortcuts import render,redirect
from django.http import HttpResponse
from firstapp.models import Employee
from django.views.decorators.csrf import csrf_exempt
def hello(request):
	msg="<h1 >this is my first my app</h1>"
	msg1="<p>this is dayal</p>"
	return HttpResponse(msg)
def EmplData(request):
	return render(request,'EmplData.html')
def showEmployeeData(request):
	obj=Employee.objects.all()
	res="Data is<br>"
	for x in obj:
		res=res+x.employeeid+"<br>"
		res=res+x.employeename+"<br>"
		res=res+x.employeegrade+"<br>"
		res=res+x.employeesalary+"<br>"
	return HttpResponse(res)
def sayHello(request):
	return redirect("http://www.google.com")

@csrf_exempt
def Save(request):
	e=request.POST.get("employeeid")
	n=request.POST.get("employeename")
	g=request.POST.get("employeegrade")
	s=request.POST.get("employeesalary")
	b=Employee(employeeid=e,employeename=n,employeegrade=g,employeesalary=s)
	b.save()
	msg="<h1>This is our Employee Data</h1>"
	return HttpResponse(msg)

	
# Create your views here.