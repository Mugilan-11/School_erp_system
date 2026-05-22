from django.urls import path
from .views import *

urlpatterns = [

    path(
        'timetable-list/',
        timetable_list,
        name='timetable_list'
    ),

    path(
        'add-timetable/',
        add_timetable,
        name='add_timetable'
    ),

    path(
        'import-timetable/',
        import_timetable,
        name='import_timetable'
    ),

]