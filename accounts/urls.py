from django.urls import path
from .views import *


urlpatterns = [

    path('', login_view, name='login'),

    path('logout/', logout_view, name='logout'),

    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),

    path('teacher-dashboard/', teacher_dashboard, name='teacher_dashboard'),

    path('student-dashboard/', student_dashboard, name='student_dashboard'),

    path('parent-dashboard/', parent_dashboard, name='parent_dashboard'),
]