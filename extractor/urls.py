from django.urls import path

from .views import (
    extractor_upload,
    row_selection,
    extractor_columns,
    export_data,
)

urlpatterns = [

    path(
        "extractor/",
        extractor_upload,
        name="extractor_upload",
    ),

    path(
        "extractor-rows/",
        row_selection,
        name="row_selection",
    ),

    path(
        "extractor-columns/",
        extractor_columns,
        name="extractor_columns",
    ),

    path(
        "export-data/",
        export_data,
        name="export_data",
    ),

]