from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect
from django.shortcuts import render

import pandas as pd

from accounts.decorators import role_required

from students.models import Student

from .forms import (
    FeeForm,
    FeeExcelUploadForm,
)
from .models import Fee


@role_required(
    "ADMIN",
    "TEACHER",
    "STUDENT",
    "PARENT",
)
def fee_list(request):

    fees = (
        Fee.objects
        .select_related("student")
        .all()
        .order_by("-payment_date")
    )

    if request.user.role == "STUDENT":

        fees = fees.filter(
            student=request.user.student
        )

    class_filter = request.GET.get(
        "class",
        ""
    )

    if class_filter:

        fees = fees.filter(
            student__student_class=class_filter
        )

    search_query = request.GET.get(
        "search",
        ""
    ).strip()

    if search_query:

        fees = fees.filter(
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
        )

    paginator = Paginator(
        fees,
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
        "fees/fee_list.html",
        {
            "page_obj": page_obj,
            "search_query": search_query,
        },
    )


@role_required(
    "ADMIN",
    "TEACHER",
)
def add_fee(request):

    if request.method == "POST":

        form = FeeForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                "fee_list"
            )

    else:

        form = FeeForm()

    return render(
        request,
        "fees/add_fee.html",
        {
            "form": form
        },
    )


@role_required(
    "ADMIN",
    "TEACHER",
)
def import_fees(request):

    if request.method == "POST":

        form = FeeExcelUploadForm(
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

                    Fee.objects.create(

                        student=student,

                        amount=row[
                            "amount"
                        ],

                        payment_date=row.get(
                            "payment_date"
                        ),

                        status=row[
                            "status"
                        ],

                        remarks=row.get(
                            "remarks",
                            "",
                        ),
                    )

                except Student.DoesNotExist:
                    continue

            return redirect(
                "fee_list"
            )

    else:

        form = FeeExcelUploadForm()

    return render(
        request,
        "fees/import_fees.html",
        {
            "form": form
        },
    )