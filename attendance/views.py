from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

import pandas as pd

from students.models import Student

from .models import Attendance

from .forms import (
    AttendanceForm,
    AttendanceExcelUploadForm
)


@login_required
def attendance_list(request):

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

        attendance_records = Attendance.objects.filter(
            student=student
        ).order_by('-date')

    # ADMIN / TEACHER VIEW

    else:

        attendance_records = Attendance.objects.all().order_by('-date')

        class_filter = request.GET.get('class')

        if class_filter:

            attendance_records = attendance_records.filter(
                student__student_class=class_filter
            )

    context = {

        'attendance_records': attendance_records

    }

    return render(
        request,
        'attendance/attendance_list.html',
        context
    )


@login_required
def mark_attendance(request):

    if request.user.role not in [
        'ADMIN',
        'TEACHER'
    ]:
        return redirect('login')

    if request.method == 'POST':

        form = AttendanceForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('attendance_list')

    else:

        form = AttendanceForm()

    context = {

        'form': form

    }

    return render(
        request,
        'attendance/mark_attendance.html',
        context
    )


@login_required
def import_attendance(request):

    if request.user.role not in [
        'ADMIN',
        'TEACHER'
    ]:
        return redirect('login')

    if request.method == 'POST':

        form = AttendanceExcelUploadForm(
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

                Attendance.objects.create(

                    student=student,

                    date=row['date'],

                    status=row['status']

                )

            return redirect('attendance_list')

    else:

        form = AttendanceExcelUploadForm()

    context = {

        'form': form

    }

    return render(
        request,
        'attendance/import_attendance.html',
        context
    )