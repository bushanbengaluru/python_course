from django.shortcuts import render
from django.http import HttpResponse
from.models import Employee

# Create your views here.
def firstview(request):
    # return HttpResponse("Hello world")
    if request.method == "GET":
        return render(request, "firstapp/add.html", {"name": "Django"})
    elif request.method == "POST":
        v1 = request.POST['t1']
        v2 = request.POST['t2']
        try:
            result = int(v1) + int(v2)
            name = f"Result is {result}"
        except ValueError:
            name = "Please enter valid integers"
        return render(request, "firstapp/add.html", {"result": result})
    
def insertview(request):
    if request.method == "GET":
        return render(request, "firstapp/insert.html")
    elif request.method == "POST":
        eid = (request.POST['eid'])
        ename = request.POST['ename']
        esal = (request.POST['esal'])
        try:
            emps = Employee.objects.create(eid=eid, ename=ename, esal=esal)
        except ValueError:
            name = "Please enter valid data"
        return render(request, "firstapp/insert.html", {"msg": "Data Inserted Successfully"})

def welcomeview(request):
    if request.method == "GET":
        return render(request, "firstapp/welcome.html")  # Pass the employee records to the template
    else:
        return HttpResponse("Invalid request method")  # Handle other request methods if needed