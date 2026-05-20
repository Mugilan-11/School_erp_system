from django.urls import path
from .views import *


urlpatterns = [

    path(
        'attendance-list/',
        attendance_list,
        name='attendance_list'
    ),

    path(
        'mark-attendance/',
        mark_attendance,
        name='mark_attendance'
    ),
    path(
    'import-attendance/',
    import_attendance,
    name='import_attendance'
),
]