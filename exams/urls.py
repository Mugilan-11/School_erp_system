from django.urls import path

from . import views


urlpatterns = [

    # =====================================
    # RESULT LIST
    # =====================================

    path(
        'result-list/',
        views.result_list,
        name='result_list'
    ),

    # =====================================
    # ADD RESULT
    # =====================================

    path(
        'add-result/',
        views.add_result,
        name='add_result'
    ),

    # =====================================
    # IMPORT RESULTS
    # =====================================

    path(
        'import-results/',
        views.import_results,
        name='import_results'
    ),

]