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
        'report-card/<int:id>/',
        report_card,
        name='report_card'
    ),
]