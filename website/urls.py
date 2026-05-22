from django.urls import path
from .views import *

urlpatterns = [

    path(
        '',
        home,
        name='home'
    ),

    path(
        'about/',
        about,
        name='about'
    ),

    path(
        'academics/',
        academics,
        name='academics'
    ),

    path(
        'admissions/',
        admissions,
        name='admissions'
    ),

    path(
        'facilities/',
        facilities,
        name='facilities'
    ),

    path(
        'gallery/',
        gallery,
        name='gallery'
    ),

    path(
        'contact/',
        contact,
        name='contact'
    ),

    path(
        'login-options/',
        login_options,
        name='login_options'
    ),

]