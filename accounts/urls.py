from django.urls import path

from . import views


urlpatterns = [

    # =====================================
    # COMMON LOGIN
    # =====================================

    path(
        'login/',
        views.student_login,
        name='login'
    ),

    # =====================================
    # ROLE BASED LOGIN
    # =====================================

    path(
        'admin-login/',
        views.admin_login,
        name='admin_login'
    ),

    path(
        'teacher-login/',
        views.teacher_login,
        name='teacher_login'
    ),

    path(
        'student-login/',
        views.student_login,
        name='student_login'
    ),

    path(
        'parent-login/',
        views.parent_login,
        name='parent_login'
    ),

    # =====================================
    # LOGOUT
    # =====================================

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

    # =====================================
    # DASHBOARDS
    # =====================================

    path(
        'admin-dashboard/',
        views.admin_dashboard,
        name='admin_dashboard'
    ),

    path(
        'teacher-dashboard/',
        views.teacher_dashboard,
        name='teacher_dashboard'
    ),

    path(
        'student-dashboard/',
        views.student_dashboard,
        name='student_dashboard'
    ),

    path(
        'parent-dashboard/',
        views.parent_dashboard,
        name='parent_dashboard'
    ),

]