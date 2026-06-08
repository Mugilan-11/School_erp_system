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
    path(
    'import-fees/',
    import_fees,
    name='import_fees'
    ),
    path(
    "fees/",
    fee_classes,
    name="fee_classes",
    ),

    path(
        "fees/<str:class_name>/",
        fee_dashboard,
        name="fee_dashboard",
    ),
    path(
    "fees/<str:class_name>/add/",
    add_class_fee,
    name="add_class_fee",
),

    path(
        "fees/<str:class_name>/view/",
        class_fee_list,
        name="class_fee_list",
    ),
]