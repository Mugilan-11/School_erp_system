from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import ExamResult

from .forms import (
    ResultForm,
    ResultExcelUploadForm
)

from students.models import Student

import pandas as pd


@login_required
def result_list(request):

    if request.user.role not in [

        'ADMIN',
        'TEACHER',
        'STUDENT',
        'PARENT'

    ]:
        return redirect('login')

    results = ExamResult.objects.all()

    class_filter = request.GET.get('class')

    if class_filter:

        results = results.filter(
            student__student_class=class_filter
        )

    context = {

        'results': results

    }

    return render(
        request,
        'exams/result_list.html',
        context
    )


@login_required
def add_result(request):

    if request.user.role not in [

        'ADMIN',
        'TEACHER'

    ]:
        return redirect('login')

    if request.method == 'POST':

        form = ResultForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('result_list')

    else:

        form = ResultForm()

    context = {

        'form': form

    }

    return render(
        request,
        'exams/add_result.html',
        context
    )


@login_required
def import_results(request):

    if request.user.role not in [

        'ADMIN',
        'TEACHER'

    ]:
        return redirect('login')

    if request.method == 'POST':

        form = ResultExcelUploadForm(

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

                ExamResult.objects.create(

                    student=student,

                    subject=row['subject'],

                    marks=row['marks'],

                    grade=row['grade']

                )

            return redirect('result_list')

    else:

        form = ResultExcelUploadForm()

    context = {

        'form': form

    }

    return render(
        request,
        'exams/import_results.html',
        context
    )