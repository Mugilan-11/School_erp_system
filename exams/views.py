from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404

import pandas as pd

from accounts.decorators import role_required

from students.models import Student

from .forms import (
    ResultForm,
    ResultExcelUploadForm,
)

from .models import (
    ExamResult,
    SubjectMark,
)


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
                student__name__icontains=search_query
            )
            |
            Q(
                student__student_id__icontains=search_query
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
            "student_classes": Student.CLASS_CHOICES,
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

            result.save()

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
                        student_id=str(
                            row["student_id"]
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


# ==================================================
# NEW CLASS → STUDENT → RESULT WORKFLOW
# ==================================================

@role_required(
    "ADMIN",
    "TEACHER",
)
def select_class(request):

    classes = Student.CLASS_CHOICES

    return render(
        request,
        "exams/select_class.html",
        {
            "classes": classes,
        },
    )


@role_required(
    "ADMIN",
    "TEACHER",
)
def class_students(
    request,
    class_name,
):

    students = Student.objects.filter(
        student_class=class_name
    ).order_by(
        "name"
    )

    return render(
        request,
        "exams/class_students.html",
        {
            "students": students,
            "class_name": class_name,
        },
    )


@role_required(
    "ADMIN",
    "TEACHER",
)
def add_student_result(
    request,
    student_id,
):

    student = get_object_or_404(
        Student,
        id=student_id,
    )

    if request.method == "POST":

        exam_name = request.POST.get(
            "exam_name"
        )

        result = ExamResult.objects.create(
            student=student,
            exam_name=exam_name,
        )

        subjects = [
            "English",
            "Tamil",
            "Maths",
            "Science",
            "Social",
        ]

        for subject in subjects:

            mark = request.POST.get(
                subject,
                0
            )

            try:

                mark = int(mark)

            except ValueError:

                mark = 0

            SubjectMark.objects.create(
                exam_result=result,
                subject_name=subject,
                mark_obtained=mark,
                maximum_mark=100,
            )

        result.calculate_result()

        result.save()

        return redirect(
            "result_list"
        )

    return render(
        request,
        "exams/add_student_result.html",
        {
            "student": student,
        },
    )