from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect
from django.shortcuts import render

import pandas as pd

from accounts.decorators import role_required

from students.models import Student

from .forms import (
    ResultForm,
    ResultExcelUploadForm,
)
from .models import ExamResult


@role_required(
    "ADMIN",
    "TEACHER",
    "STUDENT",
    "PARENT",
)
def result_list(request):

    results = (
        ExamResult.objects
        .select_related("student")
        .all()
        .order_by("-created_at")
    )

    if request.user.role == "STUDENT":

        results = results.filter(
            student=request.user.student
        )

    class_filter = request.GET.get(
        "class",
        ""
    )

    if class_filter:

        results = results.filter(
            student__student_class=class_filter
        )

    search_query = request.GET.get(
        "search",
        ""
    ).strip()

    if search_query:

        results = results.filter(
            Q(
                student__first_name__icontains=search_query
            )
            |
            Q(
                student__last_name__icontains=search_query
            )
            |
            Q(
                student__admission_no__icontains=search_query
            )
            |
            Q(
                exam_name__icontains=search_query
            )
        )

    paginator = Paginator(
        results,
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
        "exams/result_list.html",
        {
            "page_obj": page_obj,
            "search_query": search_query,
        },
    )


@role_required(
    "ADMIN",
    "TEACHER",
)
def add_result(request):

    if request.method == "POST":

        form = ResultForm(
            request.POST
        )

        if form.is_valid():

            result = form.save()

            result.calculate_result()

            return redirect(
                "result_list"
            )

    else:

        form = ResultForm()

    return render(
        request,
        "exams/add_result.html",
        {
            "form": form,
        },
    )


@role_required(
    "ADMIN",
    "TEACHER",
)
def import_results(request):

    if request.method == "POST":

        form = ResultExcelUploadForm(
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

            for _, row in df.iterrows():

                try:

                    student = Student.objects.get(
                        admission_no=str(
                            row[
                                "admission_no"
                            ]
                        ).strip()
                    )

                    ExamResult.objects.get_or_create(

                        student=student,

                        exam_name=row[
                            "exam_name"
                        ],

                        defaults={

                            "total_marks": row.get(
                                "total_marks",
                                0,
                            ),

                            "percentage": row.get(
                                "percentage",
                                0,
                            ),

                            "grade": row.get(
                                "grade",
                                "",
                            ),
                        },
                    )

                except Student.DoesNotExist:

                    continue

            return redirect(
                "result_list"
            )

    else:

        form = ResultExcelUploadForm()

    return render(
        request,
        "exams/import_results.html",
        {
            "form": form,
        },
    )