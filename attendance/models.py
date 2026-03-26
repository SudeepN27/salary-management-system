from django.db import models
from employees.models import Employee
from django.contrib.auth.models import User

class AttendanceRecord(models.Model):
    status_choice = [('present','Present'),
                    ('absent','Absent'),
                    ('half_day','Half_Day'),
                    ('holiday','Holiday')]
    employee = models.ForeignKey(Employee,on_delete=models.PROTECT)
    date = models.DateField()
    status  = models.CharField(max_length=100,choices=status_choice)
    ot_hours = models.DecimalField(max_digits=5,decimal_places=1,default=0)
    marked_by =models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
      unique_together = ('employee', 'date')

    def __str__(self):
       return f"{self.employee} - {self.date})"

class LeaveType(models.Model):
    name = models.CharField(max_length=100)
    annual_balance = models.IntegerField(default=0)
    is_paid = models.BooleanField(default=True)


class LeaveApplication(models.Model):
    status_choice=[('pending','Pending'),
                   ('approved','Approved'),
                   ('rejected','Rejected')]
    employee = models.ForeignKey(Employee,on_delete=models.PROTECT)
    leave_type = models.ForeignKey(LeaveType,on_delete=models.PROTECT)
    from_date = models.DateField()
    to_date = models.DateField()
    reason = models.TextField(max_length=500)
    status = models.CharField(max_length=100,choices=status_choice,default='pending')
    approved_by = models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
    applied_on = models.DateTimeField(auto_now_add=True)
    
class LeaveBalance(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.PROTECT)
    leave_type = models.ForeignKey(LeaveType,on_delete=models.PROTECT)
    year = models.IntegerField()
    allocated = models.IntegerField(default=0)
    used = models.IntegerField(default=0)
    class Meta:
        unique_together = ('employee', 'leave_type', 'year')

    def __str__(self):
        return f"{self.employee} - {self.leave_type} ({self.year})"
# Create your models here.
