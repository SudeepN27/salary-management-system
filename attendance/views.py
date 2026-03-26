from django.shortcuts import render
from .models import AttendanceRecord,LeaveApplication,LeaveBalance,LeaveType
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .forms import AttendanceForm, LeaveApplicationForm  


@login_required
def attendance_list(request):
    today = timezone.now()
    attendancee = AttendanceRecord.objects.filter(date__month=today.month,date__year=today.year).select_related('employee')
    return render(request ,'attendance/attendance_list.html',{'attendancee':attendancee})

@login_required
def mark_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance:attendance_list')
    else:
            
            form = AttendanceForm()
    return render(request,'attendance/mark_attendance.html',{'form':form,'title':'mark_attendance'})


@login_required
def leave_apply(request):
    if request.method == 'POST':
        form = LeaveApplicationForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)  # don't save yet
            leave.employee = Employee.objects.get(user=request.user)   # set current employee
            leave.save()                     # now save
            return redirect('attendance:leave_balance')
    else:
        form = LeaveApplicationForm()
    return render(request, 'attendance/leave_apply.html', {
        'form': form,
        'title': 'Apply for Leave'
    })


@login_required
def leave_approve(request, pk):
    leave = get_object_or_404(LeaveApplication, pk=pk)
    if request.method == 'POST':
        action = request.POST.get('action')  # 'approve' or 'reject'
        if action == 'approve':
            leave.status = 'approved'
            leave.approved_by = request.user
        elif action == 'reject':
            leave.status = 'rejected'
        leave.save()
        return redirect('attendance:attendance_list')
    return render(request, 'attendance/leave_approve.html', {'leave': leave})


@login_required
def leave_balance(request):
    balances = LeaveBalance.objects.filter(employee__user=request.user,
        year=timezone.now().year
    ).select_related('leave_type')
    return render(request, 'attendance/leave_balance.html', {'balances': balances})




# Create your views here.
