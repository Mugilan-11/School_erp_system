from django.urls import path

from .views import add_student
from .views import delete_student
from .views import edit_student
from .views import import_students
from .views import student_list

urlpatterns = [
    path(
        "student-list/",
        student_list,
        name="student_list",
    ),
    path(
        "add-student/",
        add_student,
        name="add_student",
    ),
    path(
        "edit-student/<int:id>/",
        edit_student,
        name="edit_student",
    ),
    path(
        "delete-student/<int:id>/",
        delete_student,
        name="delete_student",
    ),
    path(
        "import-students/",
        import_students,
        name="import_students",
    ),
]