from django.urls import path


from .views import (
    import_class_students,
    student_classes,
    student_list,
    add_student,
    edit_student,
    delete_student,
    import_students,
    student_dashboard,
    class_student_list,
    student_profile,
    student_years,
)

urlpatterns = [

    path(
        "students/",
        student_years,
        name="student_years",
    ),
    path(
    "students/<int:year_id>/",
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
    "students/<int:year_id>/<str:class_name>/",
    student_dashboard,
    name="student_dashboard",
),

path(
    "students/<int:year_id>/<str:class_name>/view/",
    class_student_list,
    name="class_student_list",
),
path(
    "students/<int:year_id>/<str:class_name>/import/",
    import_class_students,
    name="import_class_students",
),
path(
    "student-profile/<int:student_id>/",
    student_profile,
    name="student_profile",
),


]