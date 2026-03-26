from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns= [

    path('',views.attendance_list, name='attendance_list'),
    path('mark/', views.mark_attendance,name='mark_attendance'),
    path('leave/apply/', views.leave_apply, name='leave_apply'),
    path('leave/<int:pk>/approve/', views.leave_approve, name ='leave_approve'),
    path('leave/balance/', views.leave_balance, name='leave_balance')

]