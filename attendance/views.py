from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect
from django.shortcuts import render

import pandas as pd

from accounts.decorators import role_required

from students.models import Student

from .forms import (
    AttendanceForm,
    AttendanceExcelUploadForm,
)
from .models import Attendance


@role_required(
    "ADMIN",
    "TEACHER",
    "STUDENT",
    "PARENT",
)
def attendance_list(request):

    if request.user.role == "STUDENT":

        student = request.user.student

        attendance_records = (
            Attendance.objects
            .filter(student=student)
            .select_related("student")
            .order_by("-date")
        )

    else:

        attendance_records = (
            Attendance.objects
            .select_related("student")
            .all()
            .order_by("-date")
        )

        class_filter = request.GET.get(
            "class",
            ""
        )

        if class_filter:

            attendance_records = (
                attendance_records.filter(
                    student__student_class=class_filter
                )
            )

        search_query = request.GET.get(
            "search",
            ""
        ).strip()

        if search_query:

            attendance_records = (
                attendance_records.filter(
                    Q(
                        student__first_name__icontains=search_query
                    )
                    |
                    Q(
                        student__last_name__icontains=search_query
                    )
                    |
                    Q(
                        student__student_id__icontains=search_query
                    )
                )
            )

    paginator = Paginator(
        attendance_records,
        15,
    )

    page_number = request.GET.get(
        "page"
    )

    page_obj = paginator.get_page(
        page_number
    )

    return render(
        request,
        "attendance/attendance_list.html",
        {
            "page_obj": page_obj,
            "search_query": request.GET.get(
                "search",
                "",
            ),
        },
    )


@role_required(
    "ADMIN",
    "TEACHER",
)
def mark_attendance(request):

    if request.method == "POST":

        form = AttendanceForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                "attendance_list"
            )

    else:

        form = AttendanceForm()

    return render(
        request,
        "attendance/mark_attendance.html",
        {
            "form": form
        },
    )


@role_required(
    "ADMIN",
    "TEACHER",
)
def import_attendance(request):

    if request.method == "POST":

        form = AttendanceExcelUploadForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():

            excel_file = request.FILES[
                "excel_file"
            ]

            df = pd.read_excel(
                excel_file
            )

            imported_count = 0

            for _, row in df.iterrows():

                try:

                    student = Student.objects.get(
                        student_id=str(
                            row[
                                "student_id"
                            ]
                        ).strip()
                    )

                    _, created = (
                        Attendance.objects.get_or_create(
                            student=student,
                            date=row["date"],
                            defaults={
                                "status": row["status"],
                            },
                        )
                    )

                    if created:
                        imported_count += 1

                except Student.DoesNotExist:
                    continue

            return redirect(
                "attendance_list"
            )

    else:

        form = AttendanceExcelUploadForm()

    return render(
        request,
        "attendance/import_attendance.html",
        {
            "form": form
        },
    )
