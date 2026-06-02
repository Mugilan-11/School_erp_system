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
    path(
        "edit-teacher/<int:id>/",
        edit_teacher,
        name="edit_teacher",
    ),

    path(
        "delete-teacher/<int:id>/",
        delete_teacher,
        name="delete_teacher",
    ),

]