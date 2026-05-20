from django.urls import path
from .views import *

urlpatterns = [

    path(
        'result-list/',
        result_list,
        name='result_list'
    ),

    path(
        'add-result/',
        add_result,
        name='add_result'
    ),

    path(
        'view-result/<int:id>/',
        view_result,
        name='view_result'
    ),

    path(
        'import-results/',
        import_results,
        name='import_results'
    ),

]