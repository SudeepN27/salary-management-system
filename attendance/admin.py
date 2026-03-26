from django.contrib import admin
from . models import LeaveApplication,LeaveBalance,LeaveType,AttendanceRecord


@admin.register(AttendanceRecord)
class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ['employee','date','status','ot_hours']
    list_filter = ['date','status']
    search_fields = ['employee__full_name']

@admin.register(LeaveApplication)
class LeaveApplicationAdmin(admin.ModelAdmin):
    list_display = ['employee','applied_on','status']
    list_filter = ['applied_on','status']
    search_fields = ['employee__full_name']

@admin.register(LeaveBalance)
class LeaveBalanceAdmin(admin.ModelAdmin):
    list_display = [ 'employee', 'leave_type', 'year', 'allocated', 'used']
    list_filter =['leave_type','year']
    search_fields = ['employee__full_name']

@admin.register(LeaveType)
class LeaveTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'annual_balance', 'is_paid']
    list_filter = ['annual_balance','is_paid']
    search_fields = ['name']
# Register your models here.
