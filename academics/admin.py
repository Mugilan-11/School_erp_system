from django.contrib import admin

from .models import AcademicYear


@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):

    list_display = (
        "year_name",
        "is_active",
    )

    list_editable = (
        "is_active",
    )

    search_fields = (
        "year_name",
    )