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
        "class/<str:class_name>/",
        views.class_students,
        name="class_students",
    ),

    path(
        "student/<int:student_id>/",
        views.add_student_result,
        name="add_student_result",
    ),

]