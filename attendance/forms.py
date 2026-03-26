from django import forms
from .models import AttendanceRecord,LeaveApplication

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = AttendanceRecord

        fields = ['employee', 'date', 'ot_hours','status']
        widgets = {
            'date': forms.DateInput(attrs={'type':'date'}),
        }

class LeaveApplicationForm(forms.ModelForm):
    class Meta:
        model = LeaveApplication
        fields = ['leave_type', 'from_date', 'to_date','reason']
        widgets = {
            'from_date': forms.DateInput(attrs={'type': 'date'}),
            'to_date': forms.DateInput(attrs={'type': 'date'}),
        }