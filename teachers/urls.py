from django.urls import path
from .views import *

urlpatterns = [

    path(
        'teacher-list/',
        teacher_list,
        name='teacher_list'
    ),

    path(
        'add-teacher/',
        add_teacher,
        name='add_teacher'
    ),

]