from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # WEBSITE

    path(
        '',
        include('website.urls')
    ),

    # AUTH

    path(
        '',
        include('accounts.urls')
    ),

    # ERP APPS

    path(
        '',
        include('students.urls')
    ),

    path(
        '',
        include('teachers.urls')
    ),

    path(
        '',
        include('attendance.urls')
    ),

    path(
        '',
        include('fees.urls')
    ),

    path(
        '',
        include('exams.urls')
    ),

    path(
        '',
        include('timetable.urls')
    ),
    path(
    "",
    include(
        "extractor.urls"
    )
),

    # ADMIN

    path(
        'admin/',
        admin.site.urls
    ),


]

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )