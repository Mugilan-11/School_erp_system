from django.urls import path
from .views import *


urlpatterns = [

    path(
        'timetable-list/',
        timetable_list,
        name='timetable_list'
    ),

    path(
        'class-timetable/<str:class_name>/<str:section>/',
        class_timetable,
        name='class_timetable'
    ),

    path(
        'add-timetable/',
        add_timetable,
        name='add_timetable'
    ),
]