from django.urls import path

from . import views


urlpatterns = [

    # =====================================
    # RESULT LIST
    # =====================================

    path(
        "result-list/",
        views.result_list,
        name="result_list",
    ),

    # =====================================
    # ADD RESULT (OLD)
    # =====================================

    path(
        "add-result/",
        views.add_result,
        name="add_result",
    ),

    # =====================================
    # IMPORT RESULTS
    # =====================================

    path(
        "import-results/",
        views.import_results,
        name="import_results",
    ),

    # =====================================
    # NEW CLASS → STUDENT → RESULT FLOW
    # =====================================

    path(
        "select-class/",
        views.select_class,
        name="select_class",
    ),

    path(
        "class/<str:class_name>/<str:exam_name>/",
        views.class_students,
        name="class_students",
    ),

    path(
         "student/<int:student_id>/<str:exam_name>/",
        views.add_student_result,
        name="add_student_result",
    ),
    path(
    "results/<str:class_name>/<str:exam_name>/dashboard/",
    views.exam_dashboard,
    name="exam_dashboard",
),
    path(
    "results/",
    views.result_classes,
    name="result_classes",
    ),

    path(
        "results/<str:class_name>/",
        views.result_exams,
        name="result_exams",
    ),

    path(
        "results/<str:class_name>/<str:exam_name>/",
        views.class_exam_results,
        name="class_exam_results",
    ),
    path(
    "results/<str:class_name>/<str:exam_name>/import/",
    views.import_exam_results,
    name="import_exam_results",
    ),
    path(
    "result-detail/<int:result_id>/",
    views.student_result_detail,
    name="student_result_detail",
),

]