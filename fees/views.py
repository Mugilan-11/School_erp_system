from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

import pandas as pd

from .models import Fee
from .forms import (
    FeeForm,
    FeeExcelUploadForm
)

from students.models import Student


@login_required
def fee_list(request):

    if request.user.role not in [

        'ADMIN',
        'TEACHER',
        'STUDENT',
        'PARENT'

    ]:
        return redirect('login')

    fees = Fee.objects.all()

    class_filter = request.GET.get('class')

    if class_filter:

        fees = fees.filter(
            student__student_class=class_filter
        )

    context = {

        'fees': fees

    }

    return render(
        request,
        'fees/fee_list.html',
        context
    )


@login_required
def add_fee(request):

    if request.user.role not in [

        'ADMIN',
        'TEACHER'

    ]:
        return redirect('login')

    if request.method == 'POST':

        form = FeeForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('fee_list')

    else:

        form = FeeForm()

    context = {

        'form': form

    }

    return render(
        request,
        'fees/add_fee.html',
        context
    )


@login_required
def import_fees(request):

    if request.user.role not in [

        'ADMIN',
        'TEACHER'

    ]:
        return redirect('login')

    if request.method == 'POST':

        form = FeeExcelUploadForm(

            request.POST,
            request.FILES

        )

        if form.is_valid():

            excel_file = request.FILES['excel_file']

            df = pd.read_excel(excel_file)

            for index, row in df.iterrows():

                student = Student.objects.get(
                    admission_no=row['admission_no']
                )

                Fee.objects.create(

                    student=student,

                    amount=row['amount'],

                    status=row['status']

                )

            return redirect('fee_list')

    else:

        form = FeeExcelUploadForm()

    context = {

        'form': form

    }

    return render(
        request,
        'fees/import_fees.html',
        context
    )