from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Attendance
from .forms import AttendanceForm


@login_required
def attendance_list(request):

    if request.user.role not in [
        'ADMIN',
        'TEACHER',
        'STUDENT',
        'PARENT'
    ]:
        return redirect('login')

    if request.user.role == 'STUDENT':

        student = request.user.student

        attendance_records = Attendance.objects.filter(
            student=student
        ).order_by('-date')

    else:

        attendance_records = Attendance.objects.all().order_by('-date')

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