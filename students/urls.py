from django.urls import path


from .views import (
    student_classes,
    student_list,
    add_student,
    edit_student,
    delete_student,
    import_students,
    student_dashboard,
    class_student_list,
)

urlpatterns = [

    path(
        "students/",
        student_classes,
        name="student_classes",
    ),

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
    path(
    "students/<str:class_name>/",
    student_dashboard,
    name="student_dashboard",
),

path(
    "students/<str:class_name>/view/",
    class_student_list,
    name="class_student_list",
),

]