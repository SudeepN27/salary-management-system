from django import forms
from .models  import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_id', 'full_name', 'department', 'designation', 'employment_type', 'shift', 'date_of_joining', 'gross_salary', 'daily_wage_rate', 'bank_account', 'bank_ifsc', 'bank_name', 'pan_number', 'aadhaar_number', 'email', 'phone', 'is_active']

        widgets = { 'date_of_joining': forms.DateInput(attrs={'type':'date'}),
                               
                   }