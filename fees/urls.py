from django.urls import path
from .views import *


urlpatterns = [

    path(
        'fee-list/',
        fee_list,
        name='fee_list'
    ),

    path(
        'add-fee/',
        add_fee,
        name='add_fee'
    ),
]