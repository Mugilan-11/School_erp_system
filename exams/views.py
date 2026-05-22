from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

import pandas as pd

from students.models import Student

from .models import ExamResult

from .forms import (
    ExamResultForm,
    ResultExcelUploadForm
)


@login_required
def result_list(request):

    if request.user.role not in [
        'ADMIN',
        'TEACHER',
        'STUDENT',
        'PARENT'
    ]:
        return redirect('login')

    # STUDENT VIEW

    if request.user.role == 'STUDENT':

        student = request.user.student

        results = ExamResult.objects.filter(
            student=student
        )

    # ADMIN VIEW

    elif request.user.role == 'ADMIN':

        results = ExamResult.objects.all()

        class_filter = request.GET.get('class')

        if class_filter:

            results = results.filter(
                student__student_class=class_filter
            )

    # TEACHER VIEW

    elif request.user.role == 'TEACHER':

        teacher = request.user.teacher

        results = ExamResult.objects.filter(
            student__student_class=
            teacher.assigned_class
        )

    else:

        results = ExamResult.objects.none()

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

        form = ExamResultForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('result_list')

    else:

        form = ExamResultForm()

    context = {

        'form': form

    }

    return render(
        request,
        'exams/add_result.html',
        context
    )


@login_required
def view_result(request, id):

    result = ExamResult.objects.get(id=id)

    context = {

        'result': result

    }

    return render(
        request,
        'exams/view_result.html',
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

                    exam_name=row['exam_name'],

                    total_marks=row['total_marks'],

                    percentage=row['percentage'],

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