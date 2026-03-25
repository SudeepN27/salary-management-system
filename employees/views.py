from django.shortcuts import render
from . models import Employee,Department,Designation
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import EmployeeForm
from django.shortcuts import get_object_or_404

@login_required
def employee_list(request):
    employees= Employee.objects.filter(is_active=True).select_related('department','designation')
    return render(request,'employees/employee_list.html',{'employees':employees})


@login_required
def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees:employee_list')
    else:
            form =EmployeeForm()
    return render(request,'employees/employee_form.html',{'form':form,'title':'add_employee'})


@login_required
def employee_detail(request,pk):
     employee = get_object_or_404(Employee,pk=pk)
     return render(request, 'employees/employee_detail.html',{'employee':employee})


@login_required
def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)  
    if request.method == 'POST':     
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees:employee_detail', pk=pk)
    else:                            
        form = EmployeeForm(instance=employee)
    
    return render(request, 'employees/employee_form.html', {
        'form': form,
        'title': 'Edit Employee',
        'employee': employee
    })



     



# Create your views here.
