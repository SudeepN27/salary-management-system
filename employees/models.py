from django.db import models

# Create your models here.

class Department(models.Model):
    LOCATION_CHOICE = [('head_office','Head Office'),('factory','Factory')]
    name =models.CharField(max_length=100,unique=True)
    location = models.CharField(max_length=20,choices=LOCATION_CHOICE)
    ot_applicable =models.BooleanField(default=False)
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.get_location_display()})"
    
class Designation(models.Model):
    title =models.CharField(max_length=100)
    department =models.ForeignKey(Department,on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.title}-{self.department}"
    
class SalaryStructure(models.Model):
    department = models.OneToOneField(Department,on_delete=models.PROTECT)
    basic_percent =models.DecimalField(max_digits=5,decimal_places=2)
    da_percent = models.DecimalField(max_digits=5,decimal_places=2)
    ot_rate_per_hour =models.DecimalField(max_digits=5,decimal_places=2,default=0)
    pf_applicable = models.BooleanField(default=True)
    esi_applicable = models.BooleanField(default=True)

    def __str__(self):
        return f"Structure - {self.department}"
    
class Employee(models.Model):
    EMPLOYMENT_TYPES = [
        ('permanent', 'Permanent'),
        ('contract', 'Contract'),
        ('daily_wage', 'Daily Wage'),
    ]
    SHIFT_CHOICES = [
        ('day', 'Day Shift'),
        ('night', 'Night Shift'),
    ]

    employee_id     = models.CharField(max_length=20, unique=True)
    full_name       = models.CharField(max_length=150)
    department      = models.ForeignKey(Department, on_delete=models.PROTECT)
    designation     = models.ForeignKey(Designation, on_delete=models.PROTECT)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPES)
    shift           = models.CharField(max_length=10, choices=SHIFT_CHOICES)
    date_of_joining = models.DateField()
    gross_salary    = models.DecimalField(max_digits=10, decimal_places=2)
    daily_wage_rate = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    bank_account    = models.CharField(max_length=20)
    bank_ifsc       = models.CharField(max_length=15)
    bank_name       = models.CharField(max_length=100)
    pan_number      = models.CharField(max_length=10, blank=True)
    aadhaar_number  = models.CharField(max_length=12, blank=True)
    email           = models.EmailField()
    phone           = models.CharField(max_length=15)
    is_active       = models.BooleanField(default=True)
    created_at      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee_id} — {self.full_name}"