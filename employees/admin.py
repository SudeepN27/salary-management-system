from django.contrib import admin

from .models import Department,Designation,SalaryStructure,Employee

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display =['name','location','ot_applicable']
    list_filter = ['location','ot_applicable']
    search_fields =['name']

@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display  = ['title', 'department']
    search_fields = ['title']


@admin.register(SalaryStructure)
class SalaryStructureAdmin(admin.ModelAdmin):
    list_display = ['department', 'basic_percent', 'da_percent',
                    'ot_rate_per_hour', 'pf_applicable', 'esi_applicable']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display   = ['employee_id', 'full_name', 'department',
                      'employment_type', 'shift', 'is_active']
    list_filter    = ['department', 'employment_type', 'shift', 'is_active']
    search_fields  = ['employee_id', 'full_name', 'email', 'phone']
# Register your models here.
